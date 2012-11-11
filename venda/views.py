from django.shortcuts import render
from django.http import HttpResponseRedirect

from forms import VendaForm

def cliente_venda(request):
    if request.method == 'POST': # If the form has been submitted...
        form = VendaForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            
            form.save()

            return HttpResponseRedirect('home.html') # Redirect after POST
            #return HttpResponse("Dados cadastrados com sucesso!")

    else:
        form = VendaForm() # An unbound form

    return render(request, 'home.html', {
        'form': form,
    })# Create your views here.
