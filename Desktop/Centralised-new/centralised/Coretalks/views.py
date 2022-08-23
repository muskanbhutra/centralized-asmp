from asyncio.windows_events import NULL
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Student, Speaker

def index(request):

    depart = NULL
    speaker = NULL

    if request.method == "POST":
        depart = request.POST.get('depart')
        speaker = request.POST.get('Attend')

    print(speaker)

    context = {
        'Speakers': Speaker.objects.filter(depart = depart),
        'Core_Departments': list(Speaker.objects.values_list('depart', flat=True).distinct())
    }

    return render(request, "coretalks.html", context)

@login_required(login_url='/login/')
def pref(request):

    context = {
        'Speaker': Speaker.objects.filter(depart = "CSE")
    }

    return render(request, "pref.html", context)