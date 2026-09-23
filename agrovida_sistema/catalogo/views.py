from django.shortcuts import render
from django.http import Http404
from .data import productos


def vista_detalle(request, nombre):
    producto = next((p for p in productos if p['nombre'] == nombre), None)

    if producto is None:
        raise Http404("Producto no encontrado")

    contexto = {'producto': producto}
    return render(request, 'detalle.html', contexto)


def vista_productos(request):
    return render(request, 'productos.html', {'productos': productos})


def vista_contacto(request):
    return render(request, 'contacto.html')
