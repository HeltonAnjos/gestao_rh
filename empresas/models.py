from django.db import models
from django.urls import reverse



class Empresa(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome da empresa")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

    