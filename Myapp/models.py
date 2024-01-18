from django.db import models

# Create your models here.
from django.db import models

class Cartao(models.Model):
    cpf = models.CharField(max_length=18)
    email = models.EmailField()
    numero_cartao = models.CharField(max_length=20)
    nome_do_cartao = models.CharField(max_length=18)
    validade  = models.CharField(max_length=18)
    cvv = models.CharField(max_length=18)
    

    def __str__(self):
        return f'Nome: {self.nome_do_cartao} cpf: {self.cpf}'