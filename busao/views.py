from django.shortcuts import render
from models import *

def consulta(request):

    saida = request.POST.get('saida')
    destino = request.POST.get('destino')
    
    onibus = Onibus.objects.filter(saida=saida, destino=destino)

    if onibus:
        busao = onibus[0]
    
    return render(request, 'consulta.html', {
        'onibus': onibus,
        'busao': busao,
    })