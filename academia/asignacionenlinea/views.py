from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from asignacionenlinea.models import Pedidocurso, Linea_Asignacion
from carro.carro import Carro
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
# Create your views here.

@login_required(login_url="/autenticacion/logear")
def procesarasignacion(request):
    pedidocurso=Pedidocurso.objects.create(user=request.user)
    carro=Carro(request)
    lineas_asignar=list()
    for key, value in carro.carro.items():
        lineas_asignar.append(Linea_Asignacion(
            producto_id = key,
            cantidad = value["cantidad"],
            user=request.user,
            pedidocurso = pedidocurso,)) 

    Linea_Asignacion.objects.bulk_create(lineas_asignar)

    enviarmail(
        pedidocurso=pedidocurso,
        lineas_asignar=lineas_asignar,
        nombrealumno=request.user.username,
        emailalumno=request.user.email
    )

    messages.success(request, "ASIGNACION EXITOSA")

    return redirect(".../cursoasignar")

def enviarmail(**kwargs):
    asunto="ACADEMIA USAC"
    mensaje=render_to_string("emails/pedido.html",{
        "pedidocurso": kwargs.get("pedidocurso"),
        "lineas_asignar": kwargs.get("lineas_asignar"),
        "nombrealumno": kwargs.get("nombrealumno")
    })

    mensaje_texto=strip_tags(mensaje)
    from_email="cesararmandoperezsiguantay@gmail.com"
    #to=kwargs.get("emailalumno")
    to="chechaps@gmail.com"
    send_mail(asunto, mensaje_texto,from_email,{to},html_message=mensaje)