# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('user','data_nasc','sexo', 'ativo')
    search_fields = ('user__username',)
    list_filter = ['sexo',]
    list_editable = ['ativo',]
    readonly_fields = ['cpf', 'data_nasc', 'sexo', 'estado_civil', 'ativo']
    save_on_top = True
    list_per_page = 20
    
admin.site.register(Cliente, ClienteAdmin)