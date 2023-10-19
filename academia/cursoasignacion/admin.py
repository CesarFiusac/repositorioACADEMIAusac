from django.contrib import admin
from .models import Catedratico, Curso
# Register your models here.

class CatedraticoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "Updated")

class CursoAdmin(admin.ModelAdmin):
    readonly_fields = ("created","Updated")

admin.site.register(Catedratico, CatedraticoAdmin)
admin.site.register(Curso, CursoAdmin)