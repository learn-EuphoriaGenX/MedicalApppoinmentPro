
from django.contrib import admin
from django.urls import path, include
from .views import Home, Extra
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path("", Home, name="home"),
    path("extra/", Extra, name="extra"),
    path("accounts/", include("accounts.urls"), name="accounts"),
    path("doctors/", include("doctors.urls"), name="doctors"),
    path("appointments/", include("appointments.urls"), name="appointments"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)