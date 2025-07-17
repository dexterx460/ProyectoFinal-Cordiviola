from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from .forms import UserRegisterForm, avatarform, editprofileform
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import avatar
from django.contrib import messages

from django.conf import settings # ¡Añade esta línea!

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

        return redirect('Inicio')

    form = AuthenticationForm()

    return render(request, "app1/usuarios/login.html", {"form": form})

def register(request):

      if request.method == 'POST':

            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"app1/index.html" ,  {"mensaje":"Binevenido :)"})

      else:      
            form = UserRegisterForm()     

      return render(request,"app1/usuarios/registrarse.html",  {"form":form})
  
def logout_request(request):
    logout(request)
    return redirect('Inicio')

@login_required
def editarPerfil(request):
    usuario = request.user
    
    if usuario.is_staff == True:
         print("El usuario está activo")

    if request.method == 'POST':

        miFormulario = editprofileform(request.POST, instance=usuario)

        if miFormulario.is_valid():

            miFormulario.save()

            return redirect('Inicio')

    else:

        miFormulario = editprofileform(instance=usuario)

    return render(request, "app1/usuarios/editarusuario.html", {"form": miFormulario, "usuario": usuario})


@login_required
def upload_avatar(request):
    print("DEBUG: Entrando a la vista upload_avatar.")
    
    if request.method == 'POST':

        form = avatarform(request.POST, request.FILES) 
        if form.is_valid():
            print("DEBUG: Formulario de avatar es válido.")
            
            if avatar.objects.filter(user=request.user).exists():
                old_avatar = avatar.objects.get(user=request.user)
                old_avatar.delete()
                print(f"DEBUG: Avatar existente para {request.user.username} eliminado.")
                messages.info(request, "Tu avatar anterior ha sido reemplazado.")

            Avatar = form.save(commit=False) 
            
            Avatar.user = request.user 

            Avatar.save()
            print(f"DEBUG: Avatar guardado exitosamente para usuario: {request.user.username}.")
            
            messages.success(request, "¡Tu avatar ha sido subido/actualizado exitosamente!")
            return redirect('Perfil')
        else:
            print("DEBUG: Formulario de avatar NO es válido. Errores:", form.errors)
            messages.error(request, "Hubo un error al subir el avatar. Por favor, revisa la imagen e inténtalo de nuevo.")
    else:
        form = avatarform()
        print("DEBUG: Mostrando formulario de avatar (GET request).")

    return render(request, 'app1/usuarios/avatar.html', {'form': form})

@login_required
def cambiar_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, '¡Tu contraseña ha sido actualizada exitosamente!')
            return redirect('Perfil')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error en {field}: {error}")
            messages.error(request, 'Por favor, corrige los errores a continuación.')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
        'titulo': 'Cambiar Contraseña'
    }
    return render(request, 'app1/usuarios/cambiarcontraseña.html', context)




