from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index), #este sería como el panel de acciones principal,el que al pinchar cualquiera 
    #de las opciones me redirija a books o a las otras rutas
    path("procesarlibro/",views.procesarlibro),
    path("ingresar_un_libro/",views.ingresar_un_libro),
    
    path("procesarlibro/{{book.id}}",views.procesarlibro),
    path("procesarautor/{{book.id}}",views.procesarlibro),
    path("eliminarautor/<int: author",views.eliminarautor),
]
