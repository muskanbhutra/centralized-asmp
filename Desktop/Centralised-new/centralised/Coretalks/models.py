from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

#Many to Many relationship between Speaker and Student

class Speaker(models.Model):
    speaker_id = models.IntegerField(primary_key=True)
    depart = models.TextField()
    speakerType = models.TextField()
    speakerDate = models.TextField()
    speakerMode = models.TextField()
    speakerTime = models.TextField()
    speakerBio = models.TextField()

    def __str__(self):
        return self.speaker_id

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sessions = models.ManyToManyField(Speaker, related_name='Speakers')

    def __str__(self):
        return self.user.username