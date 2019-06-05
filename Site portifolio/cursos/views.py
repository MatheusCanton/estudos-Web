from django.shortcuts import render
from cursos.models import Curso
from cursos.forms import CursoForm

def curso_form(request, sigla=None ):
    contexto = {}
    if sigla:
        curso = Curso.objects.get(sigla=sigla)        
        contexto['titulo'] = "Alterando curso {}".format(curso.sigla)
    else: 
        curso = None
        contexto['titulo'] = "Adicione um novo curso"
    form = CursoForm(request.POST or None, instance=curso)
    if request.POST:
        if form.is_valid():
            form.save()
    contexto['formulario'] = form 
    return render(request, 'curso-form.html', contexto)

def ads(request):
    return render(request, 'ads.html')

def bd(request):
    return render(request, 'bd.html')

def gti(request):
    return render(request, 'gti.html')

def si(request):
    return render(request, 'si.html')