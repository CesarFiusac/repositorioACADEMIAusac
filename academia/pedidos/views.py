'''from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from pedidos.models import Pedido, LineaAsignacion
from carro.carro import Carro
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
# Create your views here.

@login_required(login_url="/autenticacion/logear")
def procesar_asignacion(request):
    pedido=Pedido.objects.create(user=request.user)
    carro=Carro(request)
    lineas_asignar=list()
    for key, value in carro.carro.items():
        lineas_asignar.append(LineaAsignacion(
            producto_id = key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido))
        
    LineaAsignacion.objects.bulk_create(lineas_asignar)

    enviar_mail(
        pedido=pedido,
        lineas_asignar=lineas_asignar,
        nombrealumno=request.user.username,
        emailalumno=request.user.email
    )

    messages.success(request, "ASIGNACION EXITOSA")

    return redirect(".../cursoasignar")

def enviar_mail(**kwargs):
    asunto="ACADEMIA USAC"
    mensaje=render_to_string("emails/pedido.html",{
        "pedido": kwargs.get("pedido"),
        "lineas_asignacion": kwargs.get("lineas_asignacion"),
        "nombrealumno": kwargs.get("nombrealumno")
    })

    mensaje_texto=strip_tags(mensaje)
    from_email="cesararmandoperezsiguantay@gmail.com"
    #to=kwargs.get("emailalumno")
    to="chechaps@gmail.com"
    send_mail(asunto, mensaje_texto,from_email,{to},html_message=mensaje)'''