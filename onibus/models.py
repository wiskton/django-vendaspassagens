from django.db import models

# Create your models here.

class Onibus(models.Model):
	

	horario_partida = models.CharField(max_length=5)
	horario_destino = models.CharField(max_length=5)

class Poltronas(models.Model):
	STATUS = (
		(0, 'LIVRE'),
		(1, 'OCUPADO'),
	)
	
	Onibus = models.ForeignKey(Onibus)
	numeroPoltrona = models.IntegerField()
	status = models.IntegerField(max_length=2, choices=STATUS, default=0, null=False)
