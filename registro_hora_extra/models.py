from django.db import models
from django.urls import reverse
from funcionarios.models import Funcionario


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    horas = models.DecimalField(max_digits=5, decimal_places=1)
    utilizada = models.BooleanField(default=False)

    def __str__(self):
        return self.motivo
    
    def get_absolute_url(self):
        return reverse('update_funcionario', args=[self.funcionario.id])
