from django.db import models

from django.db import models
from user.models import CustomUser
class Applicant(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    application_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

