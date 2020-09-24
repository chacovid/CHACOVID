from django.db import models


class Departamentos (models.Model):
    id_dpto = models.AutoField(primary_key=True)
    ciudad = models.CharField(max_length=30)
    departamento = models.CharField(max_length=30)

    def __str__(self):
        return self.departamento

    def nombre_del_dpto(self):
        return self.departamento.replace(" ", "_")

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        db_table = "Chacovid_departamentos"


class Datos (models.Model):
    id_datos = models.AutoField(primary_key=True)
    afectados = models.CharField(max_length=30)
    duplicidad_dias = models.CharField(max_length=30)
    fallecidos = models.CharField(max_length=30)
    casos_ultimos = models.CharField(max_length=30)
    id_dpto = models.ForeignKey(Departamentos, on_delete=models.CASCADE)

    def __str__(self):
        return ' Los datos de {self.id_dpto} '.format(self=self)

    class Meta:
        verbose_name = "Dato"
        verbose_name_plural = "Datos"
        db_table = "Chacovid_datos"
