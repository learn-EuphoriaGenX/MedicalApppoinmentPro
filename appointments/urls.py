from django.urls import path
from .views import All_doctors
urlpatterns = [
    path("all-doctors/", All_doctors, name="all-doctors"),
]