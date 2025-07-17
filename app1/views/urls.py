from django.urls import path
from .views import inicio, contacto, Relaciones, ProductosPagina, PerfilPagina, eliminar_producto, mis_productos, lista_productos, subir_producto, editar_producto, SobreMi
from app1.views.usuario import login_request, logout_request, register, upload_avatar, editarPerfil, cambiar_password

urlpatterns = [
    path('Inicio/', inicio , name='Inicio'),
    path("contacto/", contacto, name="contacto"),
    path("relacionesinversores/", Relaciones, name="relaciones"),
    path("productos/", lista_productos, name="lista_productos"),
    path("login/", login_request, name="Login"),
    path("logout/", logout_request, name="Logout"),
    path("registrarse/", register, name="Registrarse"),
    path("perfil/", PerfilPagina, name="Perfil"),
    path("avatar/", upload_avatar, name="Avatar"),
    path("editarperfil/", editarPerfil, name="EditarPerfil"),
    path("sobremi/", SobreMi, name="SobreMi"),
    path("password/", cambiar_password, name="CambiarContraseña"),
    
    path("productos/eliminar/<int:producto_id>/", eliminar_producto, name="EliminarProducto"),
    path("misproductos/", mis_productos, name="MisProducto"),
    path("subirproducto/", subir_producto, name="subir_producto"),
    path("productos/editar/<int:producto_id>/", editar_producto, name="editar_producto"),
]   

