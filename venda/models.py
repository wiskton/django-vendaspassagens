from django.db import models

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