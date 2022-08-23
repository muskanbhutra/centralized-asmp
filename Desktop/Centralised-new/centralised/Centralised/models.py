from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=20, null=True)
    rollno = models.CharField(max_length=15, null=True)
    department = models.CharField(max_length=100, null=True)
    degree = models.CharField(max_length=50, null=True)
    p_email = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=15, null=True)
      