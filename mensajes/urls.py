from django.urls import path
from mensajes.views import MensajeList, MensajeCreate, MensajeDelete


urlpatterns = [
    
    path('mensaje/list', MensajeList.as_view(), name="mensaje-list" ),
    path('mensaje/create', MensajeCreate.as_view(), name="mensaje-create" ),
    path('mensaje/<pk>/delete', MensajeDelete.as_view(), name="mensaje-delete"),

]