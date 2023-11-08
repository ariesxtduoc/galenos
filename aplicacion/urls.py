from django.contrib import admin
from django.urls import include, path
from .views import index
from .views import mostrar_feriados
from .views import enviar_correo


urlpatterns = [
    path('',index,name='index'),
    path('feriados',mostrar_feriados,name='mostra_feriados'),
    path('enviar_correo', enviar_correo, name='enviar_correo'),
]