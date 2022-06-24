from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    pass

class My(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField(max_length=700)

    def __str__(self):
        return self.name

class Down(models.Model):
    name = models.CharField(max_length=150)
    height = models.IntegerField(default=2000)

    def __str__(self):
        return self.name