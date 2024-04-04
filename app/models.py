from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(models.Model):
    # GENDER_CHOICES = [
    #     ('M', 'Male'),
    #     ('F', 'Female'),
    # ]
    
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    foruser = models.CharField(max_length=1, choices=[('M', 'Male')], default='M')
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)