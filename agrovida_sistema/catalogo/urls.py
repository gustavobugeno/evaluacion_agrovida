from django.urls import path
from .views import vista_productos, vista_detalle, vista_contacto

urlpatterns = [
    path('', vista_productos, name='inicio'),
    path('productos/', vista_productos, name='productos'),
    path('detalle/<str:nombre>/', vista_detalle, name='detalle'),
    path('contacto/', vista_contacto, name='contacto'),
]
