from django.shortcuts import render


def Home(request):
    return render(request, 'home.html')

def Extra(request):
    return render(request, 'extra.html')

