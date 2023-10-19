from django.db import models

# Create your models here.

class Catedratico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    DPI = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=50)
    contraseniaconfirm = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name="Nombre_de_catedratico"
        verbose_name_plural ="Nombre_de_catedraticos"
    def __str__(self):
        return f'{self.nombre} ({self.apellido})'
    

class Curso(models.Model):
    catedratico_asignado = models.ForeignKey(Catedratico, on_delete=models.CASCADE, default=True)
    nombrecurso = models.CharField(max_length= 80, default=True)
    codigo = models.CharField(max_length= 5)
    costo = models.FloatField()
    horario = models.CharField(max_length=60)
    cupo = models.PositiveIntegerField(null=False)
    imagen = models.ImageField(upload_to="cursoasignacion", null=True, blank=True)
    disponibilidad= models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Nombre_de_curso"
        verbose_name_plural ="Nombre_de_cursos"
    def __str__(self):
        return f'{self.nombrecurso} {self.codigo} ({self.cupo})'
    

    
