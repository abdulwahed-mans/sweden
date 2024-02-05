from django.urls import path
from . import views

urlpatterns = [
    path('ders/', views.der_list, name='der_list'),
    # Add more URL patterns as needed
]
