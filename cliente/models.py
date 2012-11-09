from django.db import models
from django.contrib.auth.models import User
   

class Cliente(models.Model):
     
    SEXOS = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('I', 'Indefinido'),
    )

    ESTADO_CIVIL = (
        (0, 'Solteiro'),
        (1, 'Casado'),
    )

    user = models.OneToOneField(User)
    cpf = models.CharField(max_length=11)
    sexo = models.CharField(max_length=1, choices=SEXOS, default='I')
    data_nasc = models.DateField('Data de Nascimento',blank=True,null=True)
    estado_civil = models.IntegerField(max_length=1, choices=ESTADO_CIVIL, default=0)
    ativo = models.BooleanField(default=True)