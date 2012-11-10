# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('user', 'nome', 'data_nasc','sexo')
    search_fields = ('user__username',)
    list_filter = ['sexo',]
    #list_editable = ['ativo',]
    readonly_fields = ['nome', 'cpf', 'data_nasc', 'sexo', 'estado_civil']
    save_on_top = True
    list_per_page = 20
    
admin.site.register(Cliente, ClienteAdmin)