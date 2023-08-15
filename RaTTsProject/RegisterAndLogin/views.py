from django.shortcuts import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from django.urls import *
from django.contrib import messages


# Create your views here.


def LoginView(request):
    if request.method == 'POST':
        username = request.POST['username'].strip()
        password = request.POST['password'].strip()

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if (request.GET.get('next', '') == ''):
                print("user log in successfull")
                return redirect("profile")
                # return redirect(f'{userprofile}')
            else:
                return redirect(request.GET['next'])
        else:
            messages.error(request, "Credential Invalid !!!")
            return HttpResponse("Credential Invalid !!!")
    else:
        return render(request, "login.html")


def logout_View(request):
    auth.logout(request)
    return redirect("homepage")


def RegisterView(request):
    print(request.POST)
    if request.method == 'POST':
        first_name = request.POST['first_name']
        print(first_name, "::::::::::::::::::::::::::::::::::::::::::::")
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                print("Username already Taken")
            elif User.objects.filter(email = email).exists():
               print("Email already Taken")
            else:
                user = User.objects.create_user(first_name=first_name, email=email, username=username, password=password)
                user.save()
                print("User Created Successfully !!!")
                return redirect("SignIn")
        else:
            print("Password didn't match")

    return render(request, "registration.html", {})