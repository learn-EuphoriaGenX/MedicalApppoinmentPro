
from django.contrib import admin
from django.urls import path, include
from .views import Home, Extra
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Home, name="home"),
    path("extra/", Extra, name="extra"),
    path("accounts/", include("accounts.urls"), name="accounts"),
    path("doctors/", include("doctors.urls"), name="doctors"),
]