from django.db import models
from main.models import Employee, ProjectManager

class WFHRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='wfh_requests')
    project_manager = models.ForeignKey(ProjectManager, on_delete=models.CASCADE, related_name='wfh_requests')
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status_choices = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee.name} - {self.start_date} to {self.end_date}"