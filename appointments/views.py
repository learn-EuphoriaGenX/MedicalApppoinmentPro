from django.shortcuts import render
from doctors.models import Doctor
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def All_doctors(request):
    doctors = Doctor.objects.filter(is_account_updated = 1)
    data = {'doctors': doctors}
    return render(request, 'all_doctors.html', data)
