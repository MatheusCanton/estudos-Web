from django.shortcuts import render
from .forms import InscreverForm, EntrarForm, EsqueciForm

def esqueci(request):
    context = {}
    if request.POST:
        form = EsqueciForm(request.POST)
        if form.is_valid():
            print('Formulario esqueci Aceito')
            form.enviar_senha()
        else:
            print('Formulario esqueci negado')
            context['formulario'] = form
    return render(request, 'esqueci.html', context)

def inscrever(request):
    context = {}
    if request.POST:
        form = InscreverForm(request.POST)
        if form.is_valid():
            print('Formulario inscrever Aceito')
        else:
            print('Formulario inscrever Negado')
            context['formulario'] = form
    return render(request, 'inscrever.html', context)

def entrar(request):
    context = {}
    if request.POST:
        form = EntrarForm(request.POST)
        if form.is_valid():
            print('Formulario entrar Aceito')
        else:
            print('Formulario Entrar Negado')
            context['formulario'] = form
    return render(request, 'login.html', context)

def lembrar(request):
    return render(request, 'lembrar.html')
