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
    emergency_contact = models.CharField(max_length=20, blank=False)
    note_about_user = models.TextField(blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "dob", "emergency_contact"]

    objects = UserAccountManager()

    def __str__(self):
        return self.email
