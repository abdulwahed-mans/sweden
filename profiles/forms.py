from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['persnr', 'phone_number', 'address', 'city', 'postal_code', 'country']
