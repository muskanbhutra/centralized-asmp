from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="coretalks"),
    path('getSpeakers/<dept>', views.getSpeakers, name="getSpeakers"),
    path('addSpeakers/<speakerId>', views.addSpeakers, name="addSpeakers"),
    path('updateSpeaker', views.updateSpeaker, name="updateSpeaker")
]