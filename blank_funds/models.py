from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.BigAutoField(primary_key=True, null=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    username = models.CharField(max_length=100, unique=True)
    isAdmin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Organisation(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100, blank=True)
    about = models.TextField(default="")
    # image = models.ImageField(upload_to='images/', null=True, blank=True)
    image = models.CharField(max_length=100, null=True, blank=True)
    social = models.ManyToManyField('Social', blank=True)
    funds_required = models.IntegerField(default=0)
    funds_raised = models.IntegerField(default=0)
    # payment = models.ManyToManyField('Payment', null=True, blank=True)


class Payment(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    donor_name = models.CharField(max_length=100, null=True, blank=True)
    donor_email = models.CharField(max_length=100, null=True, blank=True)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    # amount = models.IntegerField()
    message = models.TextField(default="")
    mode = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    payment_id = models.CharField(max_length=100, null=True, blank=True)


class Social(models.Model):
    phone = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    


