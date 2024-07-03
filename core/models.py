from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do evento')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data de criação')
    local_evento = models.CharField(max_length=100, null=False, verbose_name='Local do evento')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo
