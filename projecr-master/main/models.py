# models.py
from django.db import models


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    emp_id = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    department = models.CharField(max_length=200)
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255, verbose_name="Project Name")
    description = models.TextField(verbose_name="Project Description")
    status_choices = [
        ("ongoing", "Ongoing"),
        ("completed", "Completed"),
        ("on_hold", "On Hold"),
    ]
    status = models.CharField(
        max_length=20,
        choices=status_choices,
        default="ongoing",
        verbose_name="Project Status",
    )
    assigned_employees = models.ManyToManyField(
        Employee, blank=True, verbose_name="Assigned Employees"
    )
    managers = models.ManyToManyField(
        "ProjectManager", blank=True, verbose_name="Managers"
    )

    def __str__(self):
        return self.name


class ProjectManager(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, null=False)
    email = models.EmailField(max_length=60, null=False)
    password = models.CharField(max_length=120, null=False)
    employees = models.ManyToManyField(Employee, blank=True, verbose_name="Employees")
    projects = models.ManyToManyField(Project, blank=True, verbose_name="Projects")

    def __str__(self):
        return self.name
