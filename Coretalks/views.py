from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Speaker, Student

@login_required(login_url='/login')
def index(request):

    context = {
        'speakers': list(Speaker.objects.all().values()),
        'departments': list(Speaker.objects.values_list('depart', flat=True).distinct())
    }

    return render(request, "coretalks.html", context)

def getSpeakers(request, dept):

    context = {
        'speakers': list(Speaker.objects.filter( depart = dept ).values()),
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

    return render(request, "speakers.html")