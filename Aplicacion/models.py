from django.db import models

class ciudad (models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    ciudad = models.CharField(max_length=30)
    departamento = models.CharField(max_length=30)

  

class datos (models.Model):
    id_datos = models.AutoField(primary_key=True)
    afectados = models.CharField(max_length=30)
    duplicidad_dias = models.CharField(max_length=30)
    fallecidos = models.CharField(max_length=30)
    casos_ultimos = models.CharField(max_length=30)
    id_ciudad = models.ForeignKey(ciudad, on_delete=models.CASCADE)

   



