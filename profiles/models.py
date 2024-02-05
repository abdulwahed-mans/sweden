# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    persnr = models.CharField(max_length=12, unique=True, blank=True)  # Swedish Personal Number
    phone_number = PhoneNumberField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)
    country = CountryField(blank_label='Select country', default='SE')  # Default to Sweden

    def __str__(self):
        return f"{self.user.username}'s profile"
