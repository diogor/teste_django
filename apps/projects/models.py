from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    description = models.TextField("Descrição")
    image = models.ImageField(upload_to="projects", blank=True, null=True, verbose_name="Imagem")

    def __str__(self):
        return self.name
