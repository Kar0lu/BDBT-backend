from django.db import models
from django.contrib.auth.models import AbstractUser

class Address(models.Model):
    city = models.CharField(max_length=100)
    building_number = models.CharField(max_length=10)
    street = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.city} {self.street} {self.building_number}'

class Saloon(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return f'{self.name} {self.address.city}'

class Worker(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    PESEL = models.CharField(max_length=11, null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    birth_date = models.DateField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, blank=True, null=True)
    saloon = models.ForeignKey('Saloon', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name} {self.lastname}'

class Car(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    model = models.ForeignKey('Model', on_delete=models.CASCADE)
    saloon = models.ForeignKey('Saloon', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.model}'

class Model(models.Model):
    name = models.CharField(max_length=50)
    brand =  models.ForeignKey('Brand', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.brand} {self.name}'

class Brand(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.name}'
    
class Reservation(models.Model):
    date = models.DateTimeField()
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    worker = models.ForeignKey('Worker', on_delete=models.SET_NULL, null=True, blank=True)
    customer = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.car} {self.date}'

class CustomUser(AbstractUser):
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'