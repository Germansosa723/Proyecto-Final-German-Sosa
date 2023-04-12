from django.db import models
from django.contrib.auth.models import User 

class Rutina(models.Model):
    titulo_rutina = models.CharField(max_length=30)
    tipo_de_rutina = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=120)
    creado_el = models.DateTimeField(auto_now_add=True)
    publicador = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="publicador") 
    imagen = models.ImageField(upload_to="rutinas", null=True, blank=True)

    @property
    def imagen_url(self):
        return self.imagen.url if self.imagen else ''
    def __str__(self):
        return f"{self.id} - {self.titulo_rutina}"
    
class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)



    
    