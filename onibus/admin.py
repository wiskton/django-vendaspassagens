# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *

class PoltronasInline(admin.TabularInline):
	model = Poltronas
	extra = 20

class CadOnibus(admin.ModelAdmin):
    #list_display = ('idonibus','poltrona')
    #search_fields = ('user__username',)
    #list_filter = ['sexo',]
    #list_editable = ['ativo',]
    #readonly_fields = ['cpf', 'data_nasc', 'sexo', 'estado_civil', 'ativo']
    inlines = [PoltronasInline]
    save_on_top = True
    list_per_page = 20
    
admin.site.register(Onibus, CadOnibus)