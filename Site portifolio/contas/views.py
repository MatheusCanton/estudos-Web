from django.shortcuts import render

# Create your views here.

def entrar(request):
    return render(request, 'login.html')

def esqueciASenha(request):
    return render(request, 'esqueci.html')

def lembrar(request):
    return render(request, 'lembrar.html')

def inscrever(request):
    return render(request, 'inscrever.html')
