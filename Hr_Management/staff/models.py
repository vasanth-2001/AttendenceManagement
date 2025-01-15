from django.db import models
from user.models import CustomUser
from department.models import Department

class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    join_date = models.DateField(auto_now_add=True)
    job_title = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    emergency_contact = models.CharField(max_length=100, null=True, blank=True)
    emergency_contact_phone = models.CharField(max_length=15, null=True, blank=True)
    employment_status = models.CharField(max_length=50, choices=[
        ('Active', 'Active'),
        ('On Leave', 'On Leave'),
        ('Resigned', 'Resigned'),
    ], default='Active')
