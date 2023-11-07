from django.contrib import admin
from django.urls import include, path
from .views import index
from .views import mostrar_feriados


urlpatterns = [
    path('',index,name='index'),
    path('feriados',mostrar_feriados,name='mostra_feriados'),
]