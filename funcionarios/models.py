from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from departamentos.models import Departamentos
from empresas.models import Empresa


class Funcionario(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome do funcionário')
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamentos)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('list_funcionarios')