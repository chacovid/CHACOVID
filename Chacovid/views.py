from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

def home(request):
    return render(request, "home.html")

def permisos(request):
    return render(request, "permisos.html")

def cuidados(request):
     return render(request, 'cuidados.html')

def asistencia(request):
     return render(request, 'asistencia.html')

def mapa(request):
     return render(request, 'mapa.html')