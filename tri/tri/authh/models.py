from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from tri.authh.managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )
    USERNAME_FIELD = 'email'

    objects = AppUserManager()

class Profile(models.Model):
    first_name = models.CharField(
        max_length=25
    )
    last_name = models.CharField(
        max_length=25
    )
    age = models.PositiveIntegerField()

    user = models.OneToOneField(
        AppUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )
