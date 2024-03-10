from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import *
from django.contrib.auth.hashers import check_password


class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        if email:
            user = Employee.objects.filter(email=email).first()
            # print(type(user.password))
            # print(type(password))
            if not user:
                user = ProjectManager.objects.filter(email=email).first()
            if user and password == user.password:
                return user

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
