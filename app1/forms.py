from django import forms

class blogforms(forms.Form):
    titulo = forms.CharField()
    descripcion = forms.CharField()
    subtitulo = forms.CharField()
    contenido = forms.CharField()
    
class registrarse3(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    
class productosforms(forms.Form):
    nombre_producto = forms.CharField()
    descripcion_producto = forms.CharField()
    categoria = forms.CharField()