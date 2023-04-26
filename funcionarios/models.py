from django.db import models
from django.contrib.auth.models import User
from departamentos.models import Departamentos
from empresas.models import Empresa


class Funcionario(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome do funcionário')
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamentos)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return self.name