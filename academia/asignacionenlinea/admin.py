from django.contrib import admin
from .models import Pedidocurso, Linea_Asignacion

# Register your models here.

admin.site.register([Pedidocurso,Linea_Asignacion])