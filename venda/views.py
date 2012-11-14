from django.shortcuts import render
from django.http import HttpResponseRedirect

from models import *

def vendas(request):

    cidades = Cidade.objects.all() #cidade class

    return render(request, 'home.html', {
        'cidades': cidades,
    })# Create your views here.


def consulta(request):

    saida = request.POST.get('saida')
    destino = request.POST.get('destino')
    #preco = request.POST.get('preco')

    vendas = Venda.objects.filter(saida=saida) #cidade class
    vendas = Venda.objects.filter(destino=destino) #cidade class
    #vendas = Venda.objects.filter(preco=preco) #cidade class
    
    return render(request, 'consulta.html', {
        'vendas': vendas,
    })# Create your views here.

def horarioonibus(request):

    horariop = request.POST.get('horariop')
    

    horarios = Venda.objects.filter(horariop=horariop) #cidade class
    "######"
    print horarios
    "#######" 

    return render(request, 'consulta.html', {
        'horarios': horarios,
    })# Create your views here.    


def escolherlugar(request): #aqui ele joga para a tela onde escolhe o lugar do busao
    data_saida = request.POST.get('data_saida')
    data_destino = request.POST.get('data_destino')

    lugar = Venda.objects.filter(data_saida=data_saida) #cidade class
    lugar = Venda.objects.filter(data_saida=data_saida) #cidade class
    
    return render(request, 'consultalugar.html', {
        'lugar': lugar,
    })
