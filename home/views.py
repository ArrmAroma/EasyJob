from turtle import home
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import *





def Home(request):
    return render(request,'home/index.html')

def FindJob(request):
    return render(request,'home/FindJob.html')

def Login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)
        user = User.objects.get(email=email)
        print(user)
        if user:
            auth_user = authenticate(request, username=user.username, password=password)
            if auth_user is not None: #login success
                login(request, auth_user)
                return redirect('/')
            else:
                return redirect('login')
    else:
        return render(request, 'home/login.html')


def CompRegister(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        compname = request.POST['compname']
        category = request.POST['category']
        phone = request.POST['phone']
        print(email, password, compname, category, phone)
        entrepre = Entrepreneur.objects.filter(Q(compname=compname) | Q(email=email))
        print(entrepre)
        if entrepre:
            return redirect('/CompRegister')
        else:
            entrepre = Entrepreneur.objects.create(compname = compname, password = password , email = email , category = category , phone = phone)
            entrepre.save()
            return redirect('login')
    else:
        return render(request, 'home/CompRegister.html')

# def Register(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
        
#         print(username, email, password,)
#         member = Member.objects.filter(Q(email=email))
#         print(member)
#         if member:
#             return redirect('/CompRegister')
#         else:
#            member = Member.objects.create(username = username, password = password , email = email)
#             member.save()
#             return redirect('login')
#     else:
#         return render(request, 'home/CompRegister.html')

def Register(request):
    return render(request,'home/register.html')

def Myjob(request):
    return render(request,'home/myjob.html')

def AddJob(request):
    return render(request,'home/AddJob.html')

