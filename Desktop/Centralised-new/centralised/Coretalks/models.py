from django.db import models
from django.contrib.auth.models import User

#Many to Many relationship between Speaker and Student

class Speaker(models.Model):
    speaker_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, default='Elon Musk')
    disc = models.TextField(default='Hey, I am the Founder of SpaceX and I want to take humanity to mars')
    depart = models.CharField(max_length=50, default="CSE")
    degree = models.CharField(max_length=20, default="BTech")
    city = models.CharField(max_length=100, default="Washington DC")
    country = models.CharField(max_length=100, default="USA")

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sessions = models.ManyToManyField(Speaker, related_name='Speakers')

    def __str__(self):
        return self.user.username