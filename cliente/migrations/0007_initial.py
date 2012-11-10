# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cliente'
        db.create_table('cliente_cliente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('cpf', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sexo', self.gf('django.db.models.fields.CharField')(default=0, max_length=1)),
            ('estado_civil', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('telefone', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('cep', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('estado', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('cidade', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('pais', self.gf('django.db.models.fields.IntegerField')(default=1, max_length=1)),
            ('bairro', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('endereco', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('numero', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('complemento', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('senha', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('confirmar_senha', self.gf('django.db.models.fields.CharField')(max_length=8)),
        ))
        db.send_create_signal('cliente', ['Cliente'])


    def backwards(self, orm):
        # Deleting model 'Cliente'
        db.delete_table('cliente_cliente')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'cliente.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'bairro': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'cidade': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'complemento': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'confirmar_senha': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'cpf': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'endereco': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'estado': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'estado_civil': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'pais': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '1'}),
            'senha': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'sexo': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '1'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cliente']