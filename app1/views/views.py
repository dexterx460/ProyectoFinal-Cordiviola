from django.shortcuts import render

from django.http import HttpResponse
from .models import productos
from .forms import productosforms, ProductoForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Producto
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

def respuesta(request):
    return HttpResponse("Buenas!")

def inicio(request):
    return render(request, "app1/index.html")

def contacto(request):
    return render(request, "app1/contacto.html")

def Relaciones(request):
    return render(request, "app1/Relaciones.html")

def ProductosPagina(request):
    return render(request, "app1/productos.html")

def PerfilPagina(request):
    return render(request, "app1/perfil.html")

def SobreMi(request):
    return render(request, "app1/Sobremi.html")

def productoformulario(request):
        if request.method == "POST":
            miFormulario = productosforms(request.POST)
            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                producto = productos(nombre_producto=informacion["nombre_producto"], descripcion_producto=informacion["descripcion_producto"], categoria=informacion["categoria"])
                producto.save()
                return render(request, "app1/index.html")
        else:
            miFormulario = productosforms()
        
        return render(request, "app1/formularios/productoforms.html", context={"miFormulario": miFormulario})
    
@login_required
def perfil_usuario(request):
    productos_del_usuario = Producto.objects.filter(usuario_creador=request.user).order_by('-fecha_creacion')

    context = {
        'productos_subidos': productos_del_usuario,
    }
    return render(request, 'app1/perfil.html', context)


@login_required
def subir_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False) # No guardar aún para asignar el usuario
            producto.usuario_creador = request.user # Asigna el usuario logeado como creador
            producto.save() # Ahora sí guarda el producto en la base de datos
            messages.success(request, f"El producto '{producto.nombre}' ha sido subido exitosamente.")
            return redirect('subir_producto') # Redirige a la lista de sus propios productos
    else:
        form = ProductoForm()
    
    return render(request, 'app1/SubirProducto.html', {'form': form})

# Vista para ver todos los productos (pública)
def lista_productos(request):
    productos = Producto.objects.filter(activo=True).order_by('-fecha_creacion')
    context = {
        'productos': productos
    }
    return render(request, 'app1/productos.html', context)

@login_required
def mis_productos(request): # O el nombre que tengas para tu vista de perfil/productos subidos
    # 1. Obtener los productos subidos por el usuario actualmente logeado
    # Asegúrate de que 'Producto' y 'usuario_creador' son los nombres correctos de tu modelo y campo.
    productos_subidos = Producto.objects.filter(usuario_creador=request.user).order_by('-fecha_creacion')

    # (Opcional) Agrega un print de depuración para verificar qué productos se están recuperando
    print(f"DEBUG: Productos subidos por {request.user.username}: {productos_subidos}")
    
    # 2. Crear el diccionario de contexto. ¡Aquí solo pasamos los productos!
    context = {
        'productos_subidos': productos_subidos,
    }

    return render(request, 'app1/productossubidos.html', context)



@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if producto.usuario_creador != request.user:
        messages.error(request, "No tienes permiso para eliminar este producto.")
        return redirect('MisProductos')

    if request.method == 'POST':
        producto.delete()
        messages.success(request, f"El producto '{producto.nombre}' ha sido eliminado correctamente.")
        return redirect('MisProducto')
    

    return render(request, 'confirmar_eliminar_producto.html', {'producto': producto})

@login_required
def editar_producto(request, producto_id): # La vista recibe el id del producto
    # 1. Recuperar el producto. Si no existe, devuelve un error 404.
    producto = get_object_or_404(Producto, id=producto_id)
    
    # 2. Verificar que el usuario logeado es el dueño del producto.
    if producto.usuario_creador != request.user:
        messages.error(request, "No tienes permiso para editar este producto.")
        return redirect('MisProducto') # Redirige a la página de sus productos

    if request.method == 'POST':
        # 3. Instanciar el formulario con los datos POST y los FILES,
        # y pasar la instancia existente del producto (instance=producto).
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            # 4. Guardar los cambios en el producto.
            # Django actualizará la instancia 'producto' que pasamos.
            form.save() 
            messages.success(request, f"El producto '{producto.nombre}' ha sido actualizado exitosamente.")
            return redirect('MisProducto') # Redirige a la página de tus productos después de la edición exitosa
        else:
            messages.error(request, "Hubo un error al actualizar el producto. Revisa los campos.")
    else:
        # 5. Para una petición GET, crea el formulario pre-rellenado con los datos del producto.
        form = ProductoForm(instance=producto)
    
    # Renderiza la plantilla con el formulario.
    context = {
        'form': form,
        'producto': producto, # También puedes pasar el producto para mostrar detalles adicionales
    }
    return render(request, 'app1/editarproducto.html', context)
    


        
    


