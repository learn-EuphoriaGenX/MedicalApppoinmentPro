from django.shortcuts import render, redirect
from .models import Doctor
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            doctor = Doctor.objects.get(username=username)
            if check_password(password, doctor.password):
                request.session["doctor_id"] = doctor.id  # manual login
                messages.success(request, f"{username} logged in successfully")
                return redirect("home")
            else:
                messages.error(request, "Invalid password")
        except Doctor.DoesNotExist:
            messages.error(request, "Doctor not found")

        return redirect("dlogin")


        
    return render(request, 'dlogin.html')

def Register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
    
        isDoctorExists = Doctor.objects.filter(Q(username = username)|Q( email = email)).exists()
        if not isDoctorExists:
            hashed_password = make_password(password)
            newDoctor = Doctor(username=username, email=email, password=hashed_password)
            newDoctor.save()
            messages.success(request, f"{username} Registered successfully")
            return redirect("dlogin")
        else:
            messages.error(request, f"{username} already exists")
            return redirect("dregister")

    return render(request, 'dregister.html')

def Logout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("dlogin")