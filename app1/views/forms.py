from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Producto
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import avatar


class blogforms(forms.Form):
    titulo = forms.CharField()
    descripcion = forms.CharField()
    subtitulo = forms.CharField()
    contenido = forms.CharField()
    
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
 
        help_texts = {k: "" for k in fields}
    
    
class productosforms(forms.Form):
    nombre_producto = forms.CharField()
    descripcion_producto = forms.CharField()
    categoria = forms.CharField()
    precio = forms.IntegerField()
    
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'imagen', 'activo']
        
        labels = {
            'nombre': 'Nombre del Producto',
            'descripcion': 'Descripción',
            'precio': 'Precio (€ o $)',
            'stock': 'Cantidad en Stock',
            'imagen': 'Imagen del Producto',
            'activo': 'Producto Activo',
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
        }
        
class editprofileform(UserChangeForm):
    email = forms.EmailField(label="Ingrese su email:")
    username = forms.CharField(label="Nombre de usuario")

    last_name = forms.CharField()
    first_name = forms.CharField()
    is_active = forms.BooleanField(required=False, label="¿Está activo?")

    class Meta:
        model = User
        fields = ('username', 'email', 'last_name', 'first_name', 'is_active')


class avatarform(forms.ModelForm):
    
    class Meta:
        model = avatar
        fields = ['imagen']