from django.shortcuts import render
from models import *

def consulta(request):

    saida = request.POST.get('saida')
    destino = request.POST.get('destino')
    
    onibus = Onibus.objects.filter(saida=saida, destino=destino)

    if onibus:
        busao = onibus[0]
    else:
        busao = ''
    
    return render(request, 'consulta.html', {
        'onibus': onibus,
        'busao': busao,
    })

def consulta_poltrona(request):

    id_onibus = request.POST.get('onibus')
    
    onibus = Onibus.objects.get(pk=id_onibus)
    
    return render(request, 'consultalugar.html', {
        'onibus': onibus,
    })

