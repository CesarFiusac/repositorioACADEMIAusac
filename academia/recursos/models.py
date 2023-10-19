from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Archivoscurso(models.Model):
    nombrearchivo = models.CharField(max_length=60)
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='archivo_de_curso'
        verbose_name_plural= 'archivos_de_cursos'
    
    def __str__(self):
        return self.nombrearchivo
    
class Archivo(models.Model):
    titulo = models.CharField(max_length=60)
    contenido = models.CharField(max_length= 200)
    imagen=models.ImageField(upload_to="recusos", null=True, blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    archivocurso = models.ManyToManyField(Archivoscurso)

    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='archivo'
        verbose_name_plural= 'archivos'
    
    def __str__(self):
        return self.titulo