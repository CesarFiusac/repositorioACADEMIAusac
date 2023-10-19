from django.contrib import admin
from .models import Curso

admin.site.site_header = 'ACADEMIA USAC'
admin.site.index_title = 'Gestor administrativo'
admin.site.site_title = 'Ingenieria'

# Register your models here.

admin.site.register(Curso)