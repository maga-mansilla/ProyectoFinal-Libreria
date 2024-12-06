from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from AppLibros.models import Libro, Comentario


class FormularioRegistroUsuario(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        help_text = {k: "" for k in fields}

class FormularioEdicion(UserChangeForm):
    password = None
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username',)

class FormularioCambioPassword(PasswordChangeForm):
    old_password = forms.CharField(label=("Password Actual"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label=("Nuevo Password"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label=("Repita Nuevo Password"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

class FormularioNuevoLibro(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ('usuario','titulo', 'libro', 'escritor', 'editorial', 'descripcion', 'cantidad_de_paginas','year', 'precio', 'telefonoContacto', 'emailContacto','imagenLibro')

        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'usuario_id', 'type':'hidden'}),
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'libro' : forms.Select(attrs={'class': 'form-control'}),
            'escritor' : forms.TextInput(attrs={'class': 'form-control'}),
            'editorial' : forms.TextInput(attrs={'class': 'form-control'}),        
            'descripcion' : forms.Textarea(attrs={'class': 'form-control'}),
            'cantidad_de_paginas' : forms.Textarea(attrs={'class': 'form-control'}),
            'year' : forms.TextInput(attrs={'class': 'form-control'}),
            'precio' : forms.TextInput(attrs={'class': 'form-control'}),
            'telefonoContacto' : forms.TextInput(attrs={'class': 'form-control'}),
            'emailContacto' : forms.TextInput(attrs={'class': 'form-control'}),
        }



class ActualizacionLibro(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ('usuario','titulo', 'libro', 'escritor', 'editorial', 'descripcion', 'cantidad_de_paginas','year', 'precio', 'telefonoContacto', 'emailContacto')

        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'usuario_id', 'type':'hidden'}),
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'libro' : forms.Select(attrs={'class': 'form-control'}),
            'ecritor' : forms.TextInput(attrs={'class': 'form-control'}),
            'editorial' : forms.TextInput(attrs={'class': 'form-control'}),        
            'descripcion' : forms.Textarea(attrs={'class': 'form-control'}),
            'cantidad_de_paginas' : forms.Textarea(attrs={'class': 'form-control'}),
            'year' : forms.TextInput(attrs={'class': 'form-control'}),
            'precio' : forms.TextInput(attrs={'class': 'form-control'}),
            'telefonoContacto' : forms.TextInput(attrs={'class': 'form-control'}),
            'emailContacto' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje' : forms.Textarea(attrs={'class': 'form-control'}),
        }