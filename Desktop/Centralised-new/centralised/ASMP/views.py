from django.conf import settings
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, send_mail
from django.contrib.auth.decorators import login_required
from .models import Mentor, ASMPProfile

def asmp(request):
    return render(request, "asmp.html")

@login_required(login_url='/login/')
def pref(request):
    profile = ASMPProfile.objects.filter(user=request.user).first()
    if (profile.pref_1 != None):
        return render(request, 'finish.html')
        
    context = {
        'mentors_analytics': Mentor.objects.filter(interest = "Analytics").exclude(favourites=request.user),
        'mentors_core': Mentor.objects.filter(interest = "Core engineering").exclude(favourites=request.user),
        'mentors_ci': Mentor.objects.filter(interest = "Civil Services/Govt. of").exclude(favourites=request.user),
        'mentors_design': Mentor.objects.filter(interest = "Design").exclude(favourites=request.user),
        'mentors_fin': Mentor.objects.filter(interest = "Finance").exclude(favourites=request.user),
        'mentors_it': Mentor.objects.filter(interest = "IT").exclude(favourites=request.user),
        'mentors_manc': Mentor.objects.filter(interest = "Management consulting").exclude(favourites=request.user),
        'mentors_man': Mentor.objects.filter(interest = "Management").exclude(favourites=request.user),
        'mentors_other': Mentor.objects.filter(interest = "Other").exclude(favourites=request.user),
        'mentors_re': Mentor.objects.filter(interest = "Research").exclude(favourites=request.user),
        'mentors_strat': Mentor.objects.filter(interest = "Strategy consulting").exclude(favourites=request.user),
    }
    return render(request, "pref.html", context)

def maxscore(max_mentees):
    if max_mentees == 1:
        # return 5.0
        return 30.0
    elif max_mentees == 2:
        # return 9.0
        return 50.0
    elif max_mentees == 3:
        # return 12.0
        return 70.0
    elif max_mentees == 4:
        # return 15.0
        return 90.0

def returnScore(pref):

    if pref == 1:
        # return 2
        return 10.0
    elif pref == 2:
        # return 1.5
        return 8.0
    elif pref == 3:
        # return 1
        return 5.0
    elif pref == 4:
        # return 0.8
        return 2.0
    elif pref == 5:
        # return 0.6
        return 1

# def profile(request):
#     context = {
#         'mentors_analytics': Mentor.objects.filter(interest = "Analytics"),
#         'mentors_core': Mentor.objects.filter(interest = "Core engineering"),
#         'mentors_ci': Mentor.objects.filter(interest = "Civil Services/Govt. of India"),
#         'mentors_design': Mentor.objects.filter(interest = "Design"),
#         'mentors_fin': Mentor.objects.filter(interest = "Finance"),
#         'mentors_it': Mentor.objects.filter(interest = "IT"),
#         'mentors_manc': Mentor.objects.filter(interest = "Management consulting"),
#         'mentors_man': Mentor.objects.filter(interest = "Management"),
#         'mentors_other': Mentor.objects.filter(interest = "Other"),
#         'mentors_re': Mentor.objects.filter(interest = "Research"),
#         'mentors_strat': Mentor.objects.filter(interest = "Strategy consulting"),
#     }
#     return render(request, "pref.html", context)
    
def personal_info_add(request):
    profile = ASMPProfile.objects.filter(user=request.user).first()
    context = {'profile' : profile}
    if request.POST:
        # profile.fullname = request.POST['Field1']
        # profile.rollno = request.POST['Field2']
        # profile.department = request.POST['Field3']
        # profile.degree = request.POST['Field4']
        # profile.personalEmail = request.POST['Field11']
        profile.linkedin = request.POST.get('linkedin', False)
        profile.sop = request.POST['sop']
        # profile.experience = request.POST.get('experience', False)
        # profile.goal = request.POST.get('goal', False)
        # profile.obstacle = request.POST.get('obstacle', False)
        profile.save()
        return redirect('/asmp/pref')
    return render(request, 'asmp_profile.html', context)

def update(request):
    # email = request.session['email']
    new = Mentor.objects.all().filter(
        favourites=request.user)
    ids = new.values_list('pk', flat=True)
    error_msg = None
    c = 0
    profile = ASMPProfile.objects.filter(user=request.user).first()
    profile.linkedin = request.POST.get('linkedin', False)
    profile.sop = request.POST['sop']
    # if (not profile.fullname or not profile.rollno or not profile.department or not profile.degree or not profile.contactno):
    #     error_msg = "Enter complete personal information"
    if (not profile.sop):
        error_msg = "Make sure you have filled SOP in profile section"
    elif (profile.pref_1 != None):
        error_msg = "You have already submitted your preferences. You are not allowed to do it again."
    for i in ids:
        preference = request.POST[str(i) + " preference"]
        if (preference != "0"):
            c = c+1
            for j in ids:
                if (j == i):
                    continue
                else:
                    pref_temp = request.POST[str(j) + " preference"]
                    if (pref_temp == preference):
                        error_msg = "Unique Preference required"
                    else:
                        continue

        else:
            continue
    if (c > 0):
        for i in ids:
            preference = request.POST[str(i) + " preference"]
            p = int(preference)
            if (p != 0):
                if p in range(1, c+1):
                    continue
                else:
                    error_msg = "Enter preferences in order"
            else:
                continue
    else:
        error_msg = "Enter atleast one preference"

    if not error_msg:
        for i in ids:
            preference = request.POST[str(i) + " preference"]
            mentor = Mentor.objects.get(id=request.POST[str(i)])
            if (preference != "0"):
                if (preference == "1"):
                    profile.pref_1 = mentor.id
                elif (preference == "2"):
                    profile.pref_2 = mentor.id
                elif (preference == "3"):
                    profile.pref_3 = mentor.id
                elif (preference == "4"):
                    profile.pref_4 = mentor.id
                elif (preference == "5"):
                    profile.pref_5 = mentor.id
                profile.save()
                mentor.score = mentor.score + returnScore(int(preference))
                mentor.save()
                # send_mail("Suucessful Registration (ASMP | SARC)", "Your have been successfully registered for ASMP.<br><br> Your preferences are "+profile.pref1+" > "+profile.pref2+" > " + profile.pref3+ " > " + profile.pref4+ " > " + profile.pref5 + " <br><br>Regards<br>SARC IIT Bombay", "web.sarc.iitb@gmail.com", [profile.rollno+"@iitb.ac.in", ], fail_silently=False)
            else:
                continue
        return redirect(request, '/asmp/')
    else:
        return render(request, 'wishlist.html', {'error': error_msg, 'new': new})


def wishlist(request):

    new = Mentor.objects.all().filter(
        favourites=request.user)
    ids = new.values_list('pk', flat=True)
    for i in ids:
        mentor_update = Mentor.objects.get(id=i)
        mentor_update.maxscore = maxscore(mentor_update.maxmentees)
        if float(mentor_update.score) > mentor_update.maxscore:
            mentor_update.available = False
        mentor_update.save()

    return render(request, 'wishlist.html', {'new': new})


def favourite_add(request, id):

    mentor = get_object_or_404(Mentor, id=id)
    if mentor.favourites.filter(id=request.user.id).exists():
        mentor.favourites.remove(request.user)
    else:
        mentor.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

