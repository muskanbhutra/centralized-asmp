from django.shortcuts import render
from .models import Event, Attendee

def alumination(request):

    context = {

    }

    return render(request, "alumination.html", context)