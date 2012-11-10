from django.db import models
from django.contrib.auth.models import User
   

class Cliente(models.Model):
     
    SEXOS = (
        (0, '----'),
        (1, 'Masculino'),
        (2, 'Feminino'),
    )

    ESTADO_CIVIL = (
        (0, '----'),
        (1, 'Solteiro'),
        (2, 'Casado'),
    )

    ESTADO = {
        (0, 'SAO PAULO'),
        (1, 'MINAS GERAIS'),
        (2, 'PARANA'),
        (3, 'BAHIA'),
        (4, 'GOIAS'),
    }

    CIDADES = {
        (0, 'FRANCA'),
        (1, 'SAO PAULO'),
        (2, 'RIBEIRAO PRETO'),
        (3, 'ITAU'),
        (4, 'DELFINOPOLIS'),
        (5, 'SAO SEBASTIAO DO PARAISO'),
        (6, 'SAO SEBASTIAO DO PARAISO'),
    }

    PAIS = {
        (1, 'BRASIL'),
    }

    user = models.OneToOneField(User)
    #ativo = models.BooleanField#(default=True)
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=100)
    data_nasc = models.DateField('Data de Nascimento', blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SEXOS, default=0)
    estado_civil = models.IntegerField(max_length=1, choices=ESTADO_CIVIL, default=0)
    telefone = models.CharField(max_length=13)
    celular = models.CharField(max_length=13)
    cep = models.CharField(max_length=8)
    estado = models.IntegerField(max_length=1, choices=ESTADO, default=0)
    cidade = models.IntegerField(max_length=1, choices=CIDADES, default=0)
    pais = models.IntegerField(max_length=1, choices=PAIS, default=1)
    bairro = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    numero = models.IntegerField(max_length=10)
    complemento = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    senha = models.CharField(max_length=8)
    confirmar_senha = models.CharField(max_length=8)
    




