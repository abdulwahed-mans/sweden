from django.db import models

class DER(models.Model):
    TYPE_CHOICES = [
        ('solar', 'Solar Panel'),
        ('wind', 'Wind Turbine'),
        ('battery', 'Battery Storage'),
        # Add more DER types as needed
    ]
    name = models.CharField(max_length=100)
    der_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    capacity = models.DecimalField(max_digits=10, decimal_places=2)  # In kW or kWh for batteries
    location = models.CharField(max_length=255)
    # Additional fields as needed, e.g., installation date, status, etc.

    def __str__(self):
        return self.name

class EnergyProduction(models.Model):
    der = models.ForeignKey(DER, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    production = models.DecimalField(max_digits=10, decimal_places=2)  # In kWh
    # Additional fields as needed

    def __str__(self):
        return f"{self.der.name} production at {self.timestamp}"
