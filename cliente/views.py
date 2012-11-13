from django.shortcuts import render
from django.http import HttpResponseRedirect

from forms import ClienteForm

from models import * #importa tudo de models

def cliente_cadastro(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ClienteForm(request.POST) # A form bound to the POST data

        u = User()
        u.username = request.POST.get('cpf')
        u.password = request.POST.get('senha')
        u.nome = request.POST.get('nome')
        
        user = u.save(commit=False)
        print user
        print "#####"
        form.instance.user = user
        
        if form.is_valid(): # All validation rules pass

            form.save()
            print "######"
            print u
            print "######"
            #return HttpResponseRedirect('home.html') # Redirect after POST
            #return HttpResponse("Dados cadastrados com sucesso!")

    else:
        form = ClienteForm() # An unbound form

    return render(request, 'cadastro.html', {
        'form': form,
    })


def identificar(request):

    cpf = request.POST.get('cpf')
    senha = request.POST.get('senha')
    
    cliente = Cliente.objects.filter(cpf=cpf)
    cliente = Cliente.objects.filter(senha=senha)

    # if cliente:
    #     cpf = '09317916694'
    # else:
    #     cpf = ''
    #     if verifica_senha:
    #         senha = senha[0]
    #     else:
    #         senha = ''
    
    return render(request, 'identificar.html', {
        'cliente': cliente,
    })