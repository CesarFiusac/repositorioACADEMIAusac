from django.urls import path
from . import views

urlpatterns = [
    path('', views.recursos, name='recursos'),
    #path('categoria/<int: Archivocurso_id/>', views.categoria, name='categoria'),
]