from django.shortcuts import render
from .carro import Carro
from cursoasignacion.models import Curso
from django.shortcuts import redirect

# Create your views here.

def agregar_curso(request, curso_id):
    carro = Carro(request)
    curso = Curso.objects.get(id=curso_id)
    carro.agregarcurso(Curso=curso)
    return redirect("asignacion")

def eliminar_(request, curso_id):
    carro = Carro(request)
    curso = Curso.objects.get(id=curso_id)
    carro.eliminar(Curso=curso)
    return redirect("asignacion")

def restarcurso(request, curso_id):
    carro = Carro(request)
    curso = Curso.objects.get(id=curso_id)
    carro.restar_curso(Curso=curso)
    return redirect("asignacion")

def limpiarcarro(request, curso_id):
    carro = Carro(request)
    carro.limpiar_carro
    return redirect("asignacion")