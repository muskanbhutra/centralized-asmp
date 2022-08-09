from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .models import Profile
from ASMP.models import ASMPProfile
from django.core.mail import EmailMessage, send_mail

def team(request):
    return render(request, "team.html")

def index(request):
    # email = EmailMessage(
    #     'subject',
    #     'body',
    #     settings.EMAIL_HOST_USER,
    #     ["posoxab716@aregods.com", ],
    # )

    # send_mail("Thank you for Bonding with SARC", 
    #     "Your OTP for Registering in SARC is 345789", 
    #     settings.EMAIL_HOST_USER, 
    #     ["darshanmakwana412@gmail.com", ], 
    #     fail_silently=False
    # )

    # email.fail_silently = False
    # email.send()

    return render(request, "home.html")

def team(request):
    return render(request, 'team.html')


def profile(request):
    if request.user.is_authenticated:
        context= {}
        user = Profile.objects.filter(user=request.user).first()
        context['user'] = user    
        return render(request, "profile.html", context)
    else:
        return redirect("/login/")

def login_view(request):

    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email).first()
        if user is None:
            context = {'message': 'Profile not found'}
            return render(request, 'login.html', context)
        login_profile = Profile.objects.filter(user=user).first()
        if password == login_profile.password:
            login(request, user)
            context = {'email': email, 'name': login_profile.name}
            return redirect('index')
            #return render(request, 'profile.html', context)
        context = {'message': 'Incorrect Password'}
        return render(request, 'login.html', context)
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')
        rollno = request.POST.get('rollno')
        department = request.POST.get('department')
        degree = request.POST.get('degree')
        contact = request.POST.get('contact')
        p_email = request.POST.get('p_email')

        check_user = User.objects.filter(email=email).first()
        if not email.split('@')[1]=='iitb.ac.in':
            context = {'message': 'Please register using your LDAP ID'}
            return render(request, 'register.html', context)
        if check_user:
            context = {'message': 'User already exists'}
            return render(request, 'register.html', context)

        # send_mail("Thank you for Bonding with SARC", "Your OTP for Registering in SARC is 345789", "web.sarc.iitb@gmail.com", [email, ], fail_silently=False)

        user = User(email=email, username=email)
        profile = Profile(user=user, name=name, password=password, rollno=rollno, department=department, degree=degree,contact=contact, p_email=p_email)
        ASMPprofile = ASMPProfile(user=user)
        user.save()
        profile.save()
        ASMPprofile.save()
        return redirect('login')
    return render(request, 'register.html')

# def asmp(request):
#     return render(request, "asmp.html")

def logout_view(request):
    logout(request)
    return redirect('/')

def finish(request):
    return render(request, 'finish.html')

