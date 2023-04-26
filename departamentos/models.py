from django.db import models


class Departamentos(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")

    def __str__(self):
        return self.name
