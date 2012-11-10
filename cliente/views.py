from django.shortcuts import render
from django.http import HttpResponseRedirect

from forms import ClienteForm

def cliente_cadastro(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ClienteForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            
            form.save()

            #return HttpResponseRedirect('/sucesso/') # Redirect after POST
            return HttpResponse("Dados cadastrados com sucesso!")

    else:
        form = ClienteForm() # An unbound form

    return render(request, 'cadastro.html', {
        'form': form,
    })