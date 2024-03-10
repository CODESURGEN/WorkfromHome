from django.urls import path
from .views import *

urlpatterns = [
    path("employees/", EmployeeListCreateView.as_view()),
    path("employees/<int:pk>/", EmployeeList.as_view()),
    path("login/", LoginView.as_view()),
    path("projects/", ProjectListView.as_view()),
    path("project_managers/", ProjectManagerListView.as_view()),
    path("project_managers/<int:pk>/", ProjectManagerList.as_view()),
]