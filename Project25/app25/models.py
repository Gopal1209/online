from django.db import models

class LoginDetails(models.Model):
    username = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=30)
    contact = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
