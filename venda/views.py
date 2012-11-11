from django.shortcuts import render
from django.http import HttpResponseRedirect

from models import *

def vendas(request):

    vendas = Venda.objects.all()

    return render(request, 'home.html', {
        'vendas': vendas,
    })# Create your views here.
