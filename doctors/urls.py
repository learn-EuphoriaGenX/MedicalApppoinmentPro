from django.urls import path
from .views import Login, Register, Logout
urlpatterns = [
    path("login/", Login, name="dlogin"),
    path("register/", Register, name="dregister"),
    path("logout/", Logout, name="dlogout"),
]