from django.urls import path
from . import views

urlpatterns = [
    path('', views.procesarasignacion, name='procesar_asignacion'),
]