from asyncio.windows_events import NULL
from distutils.log import error
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Speaker, Student
import numpy as np
import pandas as pd

def updateSpeaker(request):

    sheet_url = 'https://docs.google.com/spreadsheets/d/1PXuq4EINfb3IfvKyYbjToc-yWFTrKhPeBzfrBTz1o6M/edit#gid=0'
    data = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
    data = pd.read_csv(data)

    for i in range(len(data)):
            Speaker.objects.create(
                speaker_id = i,
                depart = data.iloc[i]["Department"],
                speakerType = data.iloc[i]["Type"],
                speakerDate = data.iloc[i]["Date"],
                speakerMode = data.iloc[i]["Mode"],
                speakerTime = data.iloc[i]["Time"],
                speakerBio = data.iloc[i]["Bio"]
            )

    return redirect(index)

@login_required(login_url='/login')
def index(request):

    student = Student.objects.filter(user=request.user).first()

    if not student:
        student = Student.objects.create(user=request.user)

    context = {
        'speakers': list(Speaker.objects.all().values()),
        'departments': list(Speaker.objects.values_list('depart', flat=True).distinct()),
        'mySpeakers': list(student.sessions.values_list('speaker_id', flat=True))
    }

    return render(request, "coretalks.html", context)

def getSpeakers(request, dept):

    student = Student.objects.filter(user=request.user).first()

    if not student:
        student = Student.objects.create(user=request.user)

    context = {
        'speakers': list(Speaker.objects.filter( depart = dept ).values()),
        'mySpeakers': list(student.sessions.values_list('speaker_id', flat=True))
    }

    return render(request, "speakers.html", context)

def addSpeakers(request, speakerId):

    speaker = Speaker.objects.filter( speaker_id = speakerId ).first()
    student = Student.objects.filter(user=request.user).first()
    if not student:
        student = Student.objects.create(user=request.user)

    if student.sessions.filter( speaker_id = speaker.speaker_id).exists():
        student.sessions.remove(speaker)
    else:
        student.sessions.add(speaker)

    context = {
        'speakers': list(Speaker.objects.filter(depart = speaker.depart).values()),
        'mySpeakers': list(student.sessions.values_list('speaker_id', flat=True))
    }

    return render(request, "speakers.html", context)