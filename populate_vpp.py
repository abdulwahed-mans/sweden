import os
import django
import random
from faker import Faker
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')  # Replace 'core' with your actual project name
django.setup()

from vpp.models import DER, EnergyProduction  # Import your models

fake = Faker()

# Function to add DERs
def add_ders(n):
    for _ in range(n):
        der_type = random.choice(['solar', 'wind', 'battery'])
        name = f"{der_type.capitalize()} {fake.unique.word()}"
        capacity = random.uniform(10, 100) if der_type != 'battery' else random.uniform(5, 50)
        location = fake.address()
        
        der = DER.objects.create(
            name=name,
            der_type=der_type,
            capacity=capacity,
            location=location
        )
        add_energy_production(der, 30)  # Add 30 days of energy production data for each DER

# Function to add Energy Production data
def add_energy_production(der, days):
    for day in range(days):
        for _ in range(24):  # Assuming hourly production data
            timestamp = fake.date_time_between(start_date=f"-{days}d", end_date="now").replace(minute=0, second=0)
            production = random.uniform(0.5, 5) * (der.capacity / 100)  # Simple formula for demo purposes
            EnergyProduction.objects.create(
                der=der,
                timestamp=timestamp,
                production=production
            )

if __name__ == '__main__':
    print("Populating the VPP database with demo values...")
    add_ders(10)  # Add 10 DERs
    print("Finished populating.")
