from django.db import models

# Create your models here.

class Student(models.Model):
    # id = models.AutoField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    file = models.FileField(null=True,blank=True)
    image =models.ImageField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Car(models.Model):
     car_name = models.CharField(max_length=100)
     speed = models.IntegerField()
     def __str__(self):
           return f"{self.car_name} {self.speed}"
