from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage
# Create your views here.

def contacto(request):
    formulario_contacto=FormularioContacto()

    if request.method=="POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email = EmailMessage("Mensaje de AcademiaUSAC",
                                 "El alumno {} con correo electronico {} envia lo siguiente:\n\n\n {}".format(nombre,email,contenido),#quien lo envia
                                 "",["cesararmandoperezsiguantay@gmail.com"],reply_to=[email] )#de donde viene
            
            try:
                email.send() 
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?Invalido")
    return render(request, 'contacto/Contacto.html',{'miFormulario': formulario_contacto})