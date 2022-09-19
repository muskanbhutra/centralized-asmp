from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    id_ = models.IntegerField(primary_key=True)
    name_ = models.CharField(max_length=50)
    discription_ = models.TextField()
    date_ = models.TextField()
    location_ = models.TextField()

    def __str__(self):
        return self.id_

class Attendee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sessions = models.ManyToManyField(Event, related_name='events')

    def __str__(self):
        return self.user.username