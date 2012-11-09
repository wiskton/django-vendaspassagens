from django.db import models

# Create your models here.

class Reserva(models.Model):
	cidade = models.CharField(max_length=100)
	data = models.Date('data saida')

class Destino(models.Model):
	reserva = models.ForeignKey(Reserva)
	cidadeDestino = models.CharField(max_length=100)
	dataDestino = Date('data destino')