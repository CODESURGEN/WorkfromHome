# views.py
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializer import *
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class EmployeeListCreateView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Employee.objects.all()
        serializer_class = EmployeeSerializer(queryset, many=True)
        return Response(serializer_class.data)


class EmployeeList(APIView):
    def get(self, request, pk, format=None):
        try:
            employee = Employee.objects.get(pk=pk)
            print({employee})
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(employee)

        projects = Project.objects.filter(assigned_employees=employee)
        project_serializer = ProjectSerializer(projects, many=True)

        project_managers = set()
        for project in projects:
            project_managers.update(ProjectManager.objects.filter(projects=project))

        projectManager_serializer = ProjectManagerSerializer(
            list(project_managers), many=True
        )

        data = {
            "employee": serializer.data,
            "projects": project_serializer.data,
            "project_manager": projectManager_serializer.data,
        }
        return Response(data)


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, email=email, password=password)
        if user:
            is_manager = getattr(user, "is_manager", False)
            manager_id = getattr(user, "id", None)
            return JsonResponse(
                {"id": user.id, "is_manager": is_manager, "manager_id": manager_id},
            )
        else:
            return JsonResponse(
                {"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST
            )


class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectManagerListView(APIView):
    def get(self, request, format=None):
        queryset = ProjectManager.objects.all()
        data = []
        for manager in queryset:
            manager_serializer = ProjectManagerSerializer(manager)
            projects = Project.objects.filter(managers=manager)
            employees = Employee.objects.filter(project__in=projects).distinct()
            employees_serializer = EmployeeSerializer(employees, many=True)
            data.append(
                {
                    "manager": manager_serializer.data,
                    "employees": employees_serializer.data,
                    "projects": ProjectSerializer(projects, many=True).data,
                }
            )

        return Response(data)


class ProjectManagerList(APIView):
    def get(self, request, pk, format=None):
        try:
            manager = ProjectManager.objects.get(pk=pk)
        except ProjectManager.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = []
        serializer = ProjectManagerSerializer(manager)
        projects = Project.objects.filter(managers=manager)
        project_serializer = ProjectSerializer(projects, many=True)

        employees = Employee.objects.filter(project__in=projects).distinct()
        employees_serializer = EmployeeSerializer(employees, many=True)

        data.append(
            {
                "manager": serializer.data,
                "projects": project_serializer.data,
                "employees": employees_serializer.data,
            }
        )
        return Response(data)
