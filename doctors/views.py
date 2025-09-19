from django.shortcuts import render, redirect
from .models import Doctor
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required


# Create your views here.
def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            doctor = Doctor.objects.get(username=username)
            if check_password(password, doctor.password):
                request.session["doctor_id"] = doctor.id
                request.session['doctor_name'] = doctor.username
                request.session['doctor_email'] = doctor.email
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
    request.session["doctor_id"] = None
    request.session['doctor_name'] = None
    request.session['doctor_email'] = None
    messages.success(request, "Logged out successfully")
    return redirect("dlogin")

@login_required(login_url="dlogin")
def Profile(request):
    doctor = Doctor.objects.get(id = request.session['doctor_id'])

    if request.method == "POST":
        phone = request.POST.get("phone")
        specialization = request.POST.get("specialization")
        experience = request.POST.get("experience")
        description = request.POST.get("description")
        profile = request.FILES.get("profile")
        address = request.POST.get("address")
        fees = request.POST.get("fees")

        try:
            doctor.phone = phone
            doctor.specialization = specialization
            doctor.experience = experience
            doctor.description = description
            doctor.profile = profile
            doctor.address = address
            doctor.fees = fees
            doctor.is_account_updated = True
            doctor.save()
        
            messages.success(request, f"{request.session['doctor_name']} Updated successfully")
            return redirect("home")
        except Exception as err:
            print(err)
            messages.error(request, err)
            return redirect("dprofile")
        
    data = {'profile': doctor}


    return render(request, 'profile.html', data)