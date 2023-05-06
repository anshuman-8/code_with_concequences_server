from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.BigAutoField(primary_key=True, null=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    username = models.CharField(max_length=100, unique=True)
    isOrg = models.BooleanField(default=False)
    isAdmin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Organisation(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100, unique=True)
    funds = models.IntegerField(default=0)
    users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name
    


    