# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *

class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    #list_filter = ['ativo',]
    #list_editable = ['ativo']
    #readonly_fields = ['cliques',]
    save_on_top = True
    list_per_page = 20

class PoltronasInline(admin.TabularInline):
    model = Poltronas
    extra = 20

class OnibusAdmin(admin.ModelAdmin):
    list_display = ('saida','destino','horario_saida','horario_volta',)
    search_fields = ('saida','destino',)
    #list_filter = ['ativo',]
    #list_editable = ['ativo']
    #readonly_fields = ['cliques',]
    inlines = [PoltronasInline,]
    save_on_top = True
    list_per_page = 20  
    
admin.site.register(Onibus,OnibusAdmin)
admin.site.register(Cidade,CidadeAdmin)