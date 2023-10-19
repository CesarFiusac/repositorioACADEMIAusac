from django.shortcuts import render
from recursos.models import Archivo, Archivoscurso
# Create your views here.

def recursos(request):
    adrive = Archivo.objects.all()

    return render(request, 'recursos/recursos.html', {'adrive': adrive})

def categoria(request, Archivocurso_id):
    cate =Archivoscurso.objects.get(id=Archivocurso_id)
    adrive = Archivo.objects.filter(archivocurso=cate)
    return render(request, "recursos/categorias.html", {'cate': cate,'adrive': adrive})