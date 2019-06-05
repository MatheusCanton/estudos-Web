from django.db import models

class Curso(models.Model):
    
    nome = models.CharField(max_length=100, unique=True)
    sigla = models.CharField(max_length=5, unique=True)
    semestres = models.SmallIntegerField()
    ementa = models.TextField(null=True, blank=True)
    coordenador = models.CharField(max_length=120, null=True, blank=True)

