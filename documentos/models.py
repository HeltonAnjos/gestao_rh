from django.db import models


class Documento(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição")
