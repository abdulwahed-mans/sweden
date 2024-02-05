from django.shortcuts import render
from .models import DER, EnergyProduction

def der_list(request):
    ders = DER.objects.all()
    return render(request, 'vpp/der_list.html', {'ders': ders})

# Add more views as needed
