from django.urls import path, include
from django.contrib import admin

from .views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # For allauth
    path('register/', register, name='register'),
    path('profiles/', include('profiles.urls')),  # Link to profiles app
]

