from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mensaje(models.Model):
    mensaje = models.TextField(max_length=300)
    email = models.EmailField()
    creado_el = models.DateTimeField(auto_now_add=True) 
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes")