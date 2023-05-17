from django.db import models
from django.urls import reverse
from empresas.models import Empresa


class Departamentos(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('list_departamentos')
