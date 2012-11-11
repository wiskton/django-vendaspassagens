from django.db import models

# Create your models here.

class Venda(models.Model):
        CIDADESAIDA = (
                (0, '----'),
                (1, 'SAO PAULO'),
                (2, 'RIBEIRAO PRETO'),
                (3, 'ITAU'),
                (4, 'DELFINOPOLIS'),
                (5, 'SAO SEBASTIAO DO PARAISO'),
                (6, 'FRANCA'),
        )

        CIDADEDESTINO = (
                (0, '----'),
                (1, 'BELO HORIZONTE'),
                (2, 'RIBEIRAO PRETO'),
                (3, 'ITAU'),
                (4, 'DELFINOPOLIS'),
                (5, 'SAO SEBASTIAO DO PARAISO'),
                (6, 'FRANCA'),
        )

        saida = models.CharField(max_length=1, choices=CIDADESAIDA, default=0)
        destino = models.CharField(max_length=1, choices=CIDADEDESTINO, default=0)
        data_saida = models.DateField('Data Saida', blank=True, null=False)
        data_volta = models.DateField('Data Volta', blank=True, null=False)