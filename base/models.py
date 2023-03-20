from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone
from .managers import UserAccountManager


class UserAccount(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    dob = models.DateField(blank=False)
    email = models.EmailField(("email address"), unique=True)
    phone = models.CharField(max_length=20, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "dob"]

    objects = UserAccountManager()

    def __str__(self):
        return self.email


class Dustbin(models.Model):
    coordinates = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.location


class DustbinGroup(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    dustbins = models.ForeignKey(Dustbin, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = ["name"]

    def __str__(self):
        return self.name
