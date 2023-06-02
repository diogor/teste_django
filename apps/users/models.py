from django.db import models
from django.contrib.auth.models import AbstractUser


class ProfileChoices(models.TextChoices):
    ADMIN = "admin", "Administrador"
    USER = "user", "Usuário"


class User(AbstractUser):
    profile = models.CharField(
        choices=ProfileChoices.choices, max_length=5, default=ProfileChoices.USER
    )
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
