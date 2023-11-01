from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=100)
    cusine = models.CharField(max_length=100)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name 

class Reservation(models.Model):
    name = models.CharField(max_length=100, blank=True)
    contact = models.CharField(max_length=300)
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name # changes the name of the reservation object to the value store in the name field ofthe reservation object


class Logger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.TimeField()
    time_log2 = models.TimeField(help_text="Enter the exact date")
