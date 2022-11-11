from django.db import models
from django.contrib.auth.models import User

# Create your models here.

"cria tabela de eventos na agenda"


class Evento(models.Model):
    "cria o campo de titulo e descricao"
    titulo = models.CharField(max_length=100)

    descricao = models.TextField(null=True, blank=True)

    "cria campo de data para o evento"
    data_evento = models.DateTimeField(verbose_name='Data do evento')

    "data da criacao do evento como parametro de data automatico," \
    " de forma que o usuario nao pode altera-la "
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def ___str___(self):
        return self.titulo
