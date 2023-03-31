from django.db import models

class Rutina(models.Model):
    titulo_rutina = models.CharField(max_length=30)
    tipo_de_rutina = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=120)
    creado_el = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.id} - {self.titulo_rutina}"
