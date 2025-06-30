from django.urls import path
from .views import inicio, blogformulario, registrarteformulario, productoformulario, buscar, buscarpersona

urlpatterns = [
    path('Inicio/', inicio , name='Inicio'),
    path("blogforms/", blogformulario, name="blogform"),
    path("registrarteform/", registrarteformulario, name="registrarteform"),
    path("productoform/", productoformulario, name="productoform"),
    path("buscar/", buscar, name="buscar"),
    path("buscarusuario/", buscarpersona, name="Usuarios")
]   

