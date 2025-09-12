from django.urls import path
from .views import Login, Register, Logout, Profile
urlpatterns = [
    path("login/", Login, name="dlogin"),
    path("register/", Register, name="dregister"),
    path("logout/", Logout, name="dlogout"),
    path("profile/", Profile, name="dprofile"),
]