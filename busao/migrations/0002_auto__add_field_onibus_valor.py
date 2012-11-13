# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Onibus.valor'
        db.add_column('busao_onibus', 'valor',
                      self.gf('django.db.models.fields.DecimalField')(default=10, max_digits=8, decimal_places=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Onibus.valor'
        db.delete_column('busao_onibus', 'valor')


    models = {
        'busao.cidade': {
            'Meta': {'ordering': "('nome',)", 'object_name': 'Cidade'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'busao.onibus': {
            'Meta': {'ordering': "('data_saida',)", 'object_name': 'Onibus'},
            'data_saida': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'data_volta': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'destino': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'destino'", 'to': "orm['busao.Cidade']"}),
            'horario_saida': ('django.db.models.fields.TimeField', [], {}),
            'horario_volta': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'saida': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'saida'", 'to': "orm['busao.Cidade']"}),
            'valor': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'})
        },
        'busao.poltronas': {
            'Meta': {'ordering': "('numero',)", 'object_name': 'Poltronas'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'onibus': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['busao.Onibus']"}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'})
        }
    }

    complete_apps = ['busao']