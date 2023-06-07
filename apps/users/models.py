from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import Group
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


def add_default_group(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name="Reader")
        instance.groups.add(group)

post_save.connect(add_default_group, sender=User)
