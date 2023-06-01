from django.db import models
from django.contrib.auth.models import AbstractUser


class ProfileChoices(models.TextChoices):
    ADMIN = "admin"
    USER = "user"


class User(AbstractUser):
    profile = models.CharField(
        choices=ProfileChoices.choices, max_length=5, default=ProfileChoices.USER
    )
