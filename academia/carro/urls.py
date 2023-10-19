from django.urls import path
from . import views
app_name = "carro"

urlpatterns = [
    path("agregar_curso/<int:curso_id>/", views.agregar_curso, name="agregar_curso"),
    path("eliminar_/<int:curso_id>/", views.eliminar_, name="eliminar"),
    path("restarcurso/<int:curso_id>/", views.restarcurso, name="restar_curso"),
    path("limpiarcarro/", views.limpiarcarro, name="limpiarcarro"),
]

