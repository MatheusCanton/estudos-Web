from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import render_to_response
from .forms import ContatoForm

def home(request):
    return render(request, 'index.html')

def contato(request):
    context = {
        'titulo':'Entre em contato'
    }
    if request.POST:
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.enviar_email()
        else:
            context['formulario'] = form
    return render(request, 'contato.html', context)
