from django.db import models
from django.utils import timezone


class Prueba(models.Model):
    ID_prueba = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tipo_prueba = models.TextField()
    laboratorio = models.TextField()
    estado = models.TextField()
    encargado = models.TextField()
    comentario = models.CharField(max_length=200)
    fecha_prueba = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.fecha_prueba = timezone.now()
        self.save()

    def __str__(self):
        return self.ID_prueba

class Reporte(models.Model):
    ID_prueba = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tipo_reporte = models.TextField()
    autor = models.TextField()
    descripcion = models.CharField(max_length=200)
    fecha_reporte = models.DateTimeField(
            blank=True, null=True)

    

    def publish(self):
        self.fecha_reporte = timezone.now()
        self.save()

    def __str__(self):
        return self.ID_reporte