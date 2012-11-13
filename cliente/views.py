from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth.models import User

from forms import ClienteForm

from models import * #importa tudo de models

def cliente_cadastro(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ClienteForm(request.POST) # A form bound to the POST data

        u = User()
        u.username = request.POST.get('cpf')
        u.password = request.POST.get('senha')
        u.nome = request.POST.get('nome')
        
        u.save()
        #u = User.Objects.all().order_by('-id')[:1]
        print "####"
        print u
        
        
        if form.is_valid(): # All validation rules pass
            form.instance.user = u
            form.save()
            print "######"
            print u
            print "######"
            #form.instance.user.add(u) #nne add
            #return HttpResponseRedirect('home.html') # Redirect after POST
            #return HttpResponse("Dados cadastrados com sucesso!")

        else:
            return HttpResponse(form.errors)

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