from django.shortcuts import render
from .models import Curso
# Create your views here.

def asignacion(request):
    asignacion = Curso.objects.all()

    return render(request, 'asignacion/asignacion.html', {'asignacion': asignacion})
    