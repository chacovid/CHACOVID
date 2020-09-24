from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from ChacovidApp.models import *

def home(request):
    return render(request, "home.html")

def permisos(request):
    return render(request, "permisos.html")

def cuidados(request):
    return render(request, 'cuidados.html')

def fases(request):
    return render(request, 'fases.html')

def mapa(request):
    context = {"lista_datos": Datos.objects.all() }
    return render(request,"mapa.html",context)