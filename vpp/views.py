from django.shortcuts import render
from .models import DER, EnergyProduction

def der_list(request):
    ders = DER.objects.all()

    # Example data for charts
    labels = ["January", "February", "March", "April"]
    data = [10, 20, 30, 40]

    # Combine 'ders' with 'labels' and 'data' into the context dictionary
    context = {
        'ders': ders,
        'labels': labels,
        'data': data,
    }

    # Pass the entire context dictionary to the template
    return render(request, 'vpp/der_list.html', context)
