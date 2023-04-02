# Proyecto-Final-German-Sosa
##Bienvenido a AppGym
En este proyecto podemos encontrar cualquier tipo de rutinas sean de pierna, pecho, espalda, ect.
#### Inicio de Proyecto desde GitHub:
1. Crear un nuevo repositorio en GitHub.
1. agregarmos modulos **.gitignore** y **README.md**.
1. copiamos link de repositorio **https://github.com/Germansosa723/Proyecto-Final-German-Sosa.git**
1. Nos vamos al **Visual Studio.**

------------

### Inicio de Proyecto desde Visual Studio:
1. Empezamos abriendo la consola y escribimos: *git clone https://github.com/Germansosa723/Proyecto-Final-German-Sosa.git*. Con esto conectamos el visual con nuestro repositorio en **GitHub.**
1. django-admin startproject **Proyecto .** <---- *NO HAY QUE OLVIDARSE DEL PUNTO*
1. python manage.py startapp **AppGym** <--- *NOMBRE DE NUESTRA APP*
1. Agregamos en **settings.py** el nombre de nuestra app:

------------


**`INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

'EjemploConfig', <-- NOMBRE DE NUESTRA APP 
]`**

------------


1. Hacemos **python manage.py migrate** para crear nuestra primera migración a la base de datos.
1. Creamos la siguiente estructura de carpeta: **Templates/AppGym/Registration**
- Dentro de estas carpetas creamos el archivo **index.html**
1. Creamos la siguiente estructura de carpeta:  **Static/AppGym/css/js/assets** 
-  En las carpetas **css/js/assets** agregamos los respectivos archivos descargados.

En este punto ya tendriamos todo lo necesario para poder avanzar con los **html** y las **views**

------------


## WORK FLOW:
> Vamos a seguir una serie de pasos que nos van a ayudar a mantener la organizacion de las cosas.:

1. Creamos la **view** que necesitemos.
`
def index(request):
    return render(request, "ejemplo/indexr.html")`
1. Hacemos el **.html** respectivo a la view
*h1>
*Hola esto es el template index*/h1>*

1. Terminamos macheando con la **url **de la view
from django.contrib import admin
from django.urls import path
from ejemplo***<-nombre de nuestra app***.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index , name= 'index'), # ESTA ES LA NUEVA FUNCTION
]
###### Con este WROK FLOW podemos crear view, html y urls correctamente.

------------
## Página web:

- Corremos ***Python manage.py runserver***
- Como se tiene que ver si esta todo bien:

[![](https://kbimages.dreamhosters.com/images/2018-04_django-create-project.png)](http://https://kbimages.dreamhosters.com/images/2018-04_django-create-project.png)

------------


###Pasos para hacer un Push a github: 

Correr en la terminal: **git add .**

Correr en la terminal:**git commit -m "primer commit de mi proyecto"**

Correr en la terminal: **git push origin main**


------------

# TODO GYM FUNCIONES
###### Inicio con cuenta registrada:
- Tenemos funciones diferentes entre las cuales se encuentra:
1. "**SOBREMI"**: Se encuentra información sobre mi y el origen de la página web.
1. "**Home"**: Podemos ver el inicio de nuestra pagina.
1. "**Todas Las Rutinas"**: Template donde se encuentran todos las rutinas con botones de *detalle*, *actualizar* y *borrar*.  *Solo si sos dueño podes actualizar o borrar*.
1. "**Enviar Message"**: Un template con formulario de envio de mensajes a diferentes usarios registrados.
1. "**Mis Rutinas"**: Template solo con las rutinas ingresadas por el usuario dueño. con botones de *detalle*, *actualizar* y *borrar*. 
1. "**Nueva Rutina"**: Template usado para agregar cualquier tipo de rutina con *titulo, tipo, descripcion , creador e imagen. * Descargar la foto de google.
1. "**Perfil"**: Template con informacion del usuario con *imagen y nombre*.
1. "**mensaje"**: Template donde almacenan los mensajes recibidos de diferentes usuarios con boton para borrar.
1. "**Salir"**: Boton usado para salir de la cuenta del usuario. 

------------
###### pagina sin estar registrado:
1. "**SOBREMI**": Se encuentra información sobre mi y el origen de la página web.
1. "**Home"**: Podemos ver el inicio de nuestra pagina.
1. "**Todas las Rutinas"**:Template donde se encuentran todos las rutinas con botones de *detalle*, *actualizar* y *borrar*.  *Solo si sos dueño podes actualizar o borrar*.
1. "**Enviar Message"**: Un template con formulario de envio de mensajes a diferentes usarios registrados.
1. "**Ingresar"**: Un template para aquellos usuarios que ya se registraron con *usuario y contraseña*.
1. "**Registrarse"**: Template para registrarse como usuario, te pide agregar tu *nombre y confirmar 2 veces tu contraseña.*

------------

### Buscar
- Metodo de busqueda para encontrar la rutina que quieras, funciona con **boton** o apretando la tecla **enter.**

------------