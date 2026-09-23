from django.shortcuts import render
from data import productos

def vista_detalle(request):
    return render(request, 'detalles.html')

def vista_productos(request):
    return render(request, 'productos.html', {'productos': productos})

def vista_contacto(request):
    return render(request, 'contacto.html')