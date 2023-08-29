from django.db import models

# Create your models here.

#category of the cars
class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)


    def __str__(self):
        return self.name
    
#Vehicle Model using foreign key
class Vehicle(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price_usd = models.DecimalField(max_digits=10, decimal_places=2)
    country_made = models.CharField(max_length=50)
    wheels = models.PositiveIntegerField()
    horsepower = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=8, decimal_places=2)
    color = models.CharField(max_length=20)
    fuel_type = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

