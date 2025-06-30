from django.shortcuts import render

from django.http import HttpResponse
from .models import blog, productos, buscar, registrarse
from .forms import blogforms, registrarse3, productosforms

def respuesta(request):
    return HttpResponse("Buenas!")

def inicio(request):
    return render(request, "app1/index.html")

def blogformulario(request):
    if request.method == "POST":
        miFormulario = blogforms(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            Blog = blog(titulo=informacion["titulo"], descripcion=informacion["descripcion"], subtitulo=informacion["subtitulo"], contenido=informacion["contenido"])
            Blog.save()
            return render(request, "app1/index.html")
    else:
        miFormulario = blogforms()
    return render(request, "app1/formularios/blogforms.html", context={"miFormulario": miFormulario})

def registrarteformulario(request):
    if request.method == "POST":
        miFormulario = registrarse3(request.POST)
        if miFormulario.is_valid():
            informacion2 = miFormulario.cleaned_data
            registro = registrarse(nombre=informacion2["nombre"], apellido=informacion2["apellido"], email=informacion2["email"])
            registro.save()
            return render(request, "app1/index.html")
    else:
        miFormulario = registrarse3()
    return render(request, "app1/formularios/regisforms.html", context={"miFormulario": miFormulario})

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
    
def buscar(request):
    return render(request, "app1/formularios/busquedapersonas.html")
    

    
def buscarpersona(request):
    busqueda = request.GET.get("nombre", None) #

    if busqueda:
        nombre = registrarse.objects.filter(nombre__icontains=busqueda)
    else:
        nombre = nombre.objects.all() 
    
    return render(request, "app1/formularios/resultadospersonas.html", context={"nombre": nombre}) 
        
    


