from django.db import models
from django.contrib.auth.models import User


class Departamentos(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
