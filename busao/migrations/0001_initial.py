# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cidade'
        db.create_table('busao_cidade', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('busao', ['Cidade'])

        # Adding model 'Onibus'
        db.create_table('busao_onibus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('saida', self.gf('django.db.models.fields.related.ForeignKey')(related_name='saida', to=orm['busao.Cidade'])),
            ('destino', self.gf('django.db.models.fields.related.ForeignKey')(related_name='destino', to=orm['busao.Cidade'])),
            ('horario_saida', self.gf('django.db.models.fields.TimeField')()),
            ('horario_volta', self.gf('django.db.models.fields.TimeField')()),
            ('data_saida', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('data_volta', self.gf('django.db.models.fields.DateField')(blank=True)),
        ))
        db.send_create_signal('busao', ['Onibus'])

        # Adding model 'Poltronas'
        db.create_table('busao_poltronas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('onibus', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['busao.Onibus'])),
            ('numero', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
        ))
        db.send_create_signal('busao', ['Poltronas'])


    def backwards(self, orm):
        # Deleting model 'Cidade'
        db.delete_table('busao_cidade')

        # Deleting model 'Onibus'
        db.delete_table('busao_onibus')

        # Deleting model 'Poltronas'
        db.delete_table('busao_poltronas')


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
            'saida': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'saida'", 'to': "orm['busao.Cidade']"})
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