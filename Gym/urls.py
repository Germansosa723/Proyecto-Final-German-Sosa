"""Gym URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppGym.views import index, sobremi, RutinaList, RutinaCreate, RutinaDetail, RutinaUpdate, RutinaDelete, RutinaSearch, Login, Logout, SignUp, RutinaMineList, ProfileCreate, ProfileUpdate
from django.conf import settings
from django.conf.urls.static import static
from mensajes.urls import MensajeDelete, MensajeList, MensajeCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('sobre/mi' ,sobremi, name = 'sobremi'),
    path('rutina/list', RutinaList.as_view(), name="rutina-list"),
    path('rutina/create', RutinaCreate.as_view(), name="rutina-create"),
    path('rutina/buscar', RutinaSearch.as_view(), name="rutina-search"),
    path('rutina/<pk>/detail', RutinaDetail.as_view(), name="rutina-detail"),
    path('rutina/<pk>/update', RutinaUpdate.as_view(), name="rutina-update"),
    path('rutina/<pk>/delete', RutinaDelete.as_view(), name="rutina-delete"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('rutina/list/mine', RutinaMineList.as_view(), name="rutina-mine"),
    path('profile/create', ProfileCreate.as_view(), name="profile-create"),   
    path('profile/<pk>/update', ProfileUpdate.as_view(), name="profile-update"),
    path('mensaje/list', MensajeList.as_view(), name="mensaje-list" ),
    path('mensaje/create', MensajeCreate.as_view(), name="mensaje-create" ),
    path('mensaje/<pk>/delete', MensajeDelete.as_view(), name="mensaje-delete"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)