from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    departure_city = models.CharField(max_length=50)
    arrival_city = models.CharField(max_length=50)
    departure_date = models.DateField()
    arrival_date = models.DateField()
  
