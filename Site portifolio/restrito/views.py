from django.shortcuts import render

# Create your views here.

def notas(request):
    return render(request, 'notas.html')