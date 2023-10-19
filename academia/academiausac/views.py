from django.shortcuts import render, HttpResponse
from carro.carro import Carro

# Create your views here.

def home(request):
    carro=Carro(request)

    return render(request, 'academiausac/home.html')

def login(request):
    return render(request, 'academiausac/login.html')