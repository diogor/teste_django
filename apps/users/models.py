from django.db import models
from django.contrib.auth.models import AbstractUser


class ProfileChoices(models.TextChoices):
    ADMIN = "admin", "Administrador"
    USER = "user", "Usuário"


class User(AbstractUser):
    profile = models.CharField(
        choices=ProfileChoices.choices, max_length=5, default=ProfileChoices.USER, verbose_name="Perfil"
    )
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name="Endereço")
    city = models.CharField(max_length=255, blank=True, null=True, verbose_name="Cidade")
    state = models.CharField(max_length=2, blank=True, null=True, verbose_name="Estado")
