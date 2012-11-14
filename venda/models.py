from django.db import models
from django.utils.formats import number_format

# Create your models here.

class Cidade(models.Model):
    nome = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('nome',)
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

    def __unicode__(self):
        return self.nome

class Venda(models.Model):

        saida = models.ForeignKey(Cidade,related_name='saida')
        destino = models.ForeignKey(Cidade,related_name='destino')
        data_saida = models.DateField('Data Saida', blank=True, null=False)
        data_volta = models.DateField('Data Volta', blank=True, null=False)
        preco = models.DecimalField(max_digits=10, decimal_places=2, default=40)

class FormasPagamento(models.Model):
    
    FPAG = (
        (0, '-----'),
        (1, 'CARTAO DE CREDITO'),
    )

    formas_pagamento = models.IntegerField(max_length=2, choices=FPAG, default=0)