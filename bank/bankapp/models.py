from django.db import models

# Create your models here.
class details(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField()
    age=models.CharField(max_length=2)
    phone=models.CharField(max_length=12)
    email=models.EmailField()
    address=models.CharField(max_length=150)


class Country(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name