from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user =  models.CharField(max_length=10, blank=False, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=10, blank=False,default=False, unique=True)
    email = models.EmailField(max_length=254, blank=False,default=False, unique=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    email_confirmed = models.BooleanField(default=False)
    phone_confirmed = models.BooleanField(default=False)
    def __str__(self):
        return self.user


