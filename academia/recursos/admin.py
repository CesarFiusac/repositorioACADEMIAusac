from django.contrib import admin
from .models import Archivoscurso, Archivo

# Register your models here.

class ArchivocursoAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')

class ArchivoAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')

admin.site.register(Archivoscurso, ArchivocursoAdmin)
admin.site.register(Archivo, ArchivoAdmin)
