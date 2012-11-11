from django.db import models

# Create your models here.

class Destino(models.Model):
	cidadeDestino = models.CharField(max_length=100)
	dataDestino = models.DateField('data destino')
	hora_partida = models.CharField(max_length=5)
	hora_chegada = models.CharField(max_length=5)
	valor = models.DecimalField(max_digits=5, decimal_places=2)
	poltrona_livres = models.IntegerField(max_length=5)