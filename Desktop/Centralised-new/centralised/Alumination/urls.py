from django.urls import path
from . import views

urlpatterns = [
    path('', views.alumination, name="alumination"),
    path('events', views.events, name="events"),
    path('events/<event>', views.event, name="event"),
]