from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def mostrar_feriados(request):
    return render(request, 'aplicacion\mostra_feriados.html')