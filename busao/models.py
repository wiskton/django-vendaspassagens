# -*- coding: utf-8 -*-
from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('nome',)
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

    def __unicode__(self):
        return self.nome

class Onibus(models.Model):
    saida = models.ForeignKey(Cidade,related_name='saida')
    destino = models.ForeignKey(Cidade,related_name='destino')
    horario_saida = models.TimeField()
    horario_volta = models.TimeField()
    data_saida = models.DateField('Data Saida', blank=True, null=False)
    data_volta = models.DateField('Data Volta', blank=True, null=False)
    valor = models.DecimalField('Valor',decimal_places=2, max_digits=8)

    def todas_poltronas(self):
        return Poltronas.objects.filter(onibus=self)

    def poltronas(self):
        return Poltronas.objects.filter(onibus=self, status=0).count()

    class Meta:
        ordering = ('data_saida',)
        verbose_name = 'Onibus'
        verbose_name_plural = 'Onibus'

class Poltronas(models.Model):
    
    STATUS = (
        (0, 'LIVRE'),
        (1, 'OCUPADO'),
    )

    onibus = models.ForeignKey(Onibus)
    numero = models.IntegerField(max_length=2)
    status = models.IntegerField(max_length=1, choices=STATUS, default=0)
    
    class Meta:
        ordering = ('numero',)
        verbose_name = 'Poltrona'
        verbose_name_plural = 'Poltronas'

    def __unicode__(self):
        return '{0}'.format(self.numero)