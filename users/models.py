from django.db import models

# Create your models here.


class UserProfile(models.Model):
    name = models.CharField(max_length=40)

    username = models.CharField(max_length=40)

    parol = models.CharField()

    manzil = models.CharField()
    
