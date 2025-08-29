from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q


# Create your views here.
def Login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        userAuthenticate = authenticate(username=username, password=password)
        if userAuthenticate is not None:
            login(request, userAuthenticate)
            messages.success(request, f"{username} logged in successfully")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("login")

    return render(request, 'login.html')

def Register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
    
        isUserExist = User.objects.filter(Q(username = username)|Q( email = email)).exists()
        print(isUserExist)
        if not isUserExist:
            newUser = User.objects.create_user(username=username, email=email, password=password)
            newUser.save()
            messages.success(request, f"{username} created successfully")
            return redirect("login")
        else:
            messages.error(request, f"{username} already exists")
            return redirect("register")

    return render(request, 'register.html')


def Logout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("login")