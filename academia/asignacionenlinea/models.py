from django.db import models
from django.contrib.auth import get_user_model
from cursoasignacion.models import Curso
from django.db.models import F, Sum, FloatField

User=get_user_model()

# Create your models here.

class Pedidocurso(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
    
    @property
    def total(self):
        return self.lineaasignacion_set.aggregate(
            total=Sum(F("costo")*F("cantidad"), output_fild=FloatField())
        )["total"]

    class Meta:
        db_table='Asignaciones'
        verbose_name='asignacion'
        verbose_name_plural='asignaciones'
        ordering=['id']

class Linea_Asignacion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    asignar = models.ForeignKey(Pedidocurso, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.cantidad}curso{self.curso}'
    
    class Meta:
        db_table='lineaasignacion'
        verbose_name='Asignacion en linea'
        verbose_name_plural='asignaciones'
        ordering=['id']
    