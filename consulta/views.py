from django.shortcuts import render
from django.http import HttpResponseRedirect

from models import Consulta

def Consulta_Venda(request):

    saida_cidade = request.POST.get('cidadeDestino')
    consulta = Consulta_Venda.objects.filter(saida_cidade=cidadeDestino)

    return render(request, 'home.html', {
        'consulta': consulta,
    })