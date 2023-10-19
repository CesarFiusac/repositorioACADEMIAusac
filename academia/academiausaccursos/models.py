from django.db import models

# Create your models here.

class Curso(models.Model):
    nombrecurso = models.CharField(max_length=60)
    codigo = models.CharField(max_length= 5)
    costo = models.CharField(max_length=10)
    horario = models.CharField(max_length=60)
    cupo = models.IntegerField() 
    catedratico = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='academiausaccursos',default='')

    class Meta:
        verbose_name='Curso'
        verbose_name_plural= 'Curso'
    
    def __str__(self):
        return f'{self.nombrecurso} {self.codigo} ({self.cupo})'