#from django.http import HttpResponse,HttpResponseForbidden
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Libro, Comentario
from .forms import FormularioRegistroUsuario, FormularioCambioPassword, FormularioEdicion,ActualizacionLibro,FormularioNuevoLibro,FormularioComentario
from django.shortcuts import get_object_or_404

#HOME
class HomeView( TemplateView):
    template_name = 'home.html'

#LOGIN#
class LoginPagina(LoginView):
    template_name = 'login.html'
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')

#REGISTRO#
class RegistroPagina(FormView):
    template_name = 'registro.html'
    form_class = FormularioRegistroUsuario
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegistroPagina, self).get(*args, **kwargs)

#EDICION
class UsuarioEdicion(LoginRequiredMixin,UpdateView):
    form_class = FormularioEdicion
    template_name= 'edicionPerfil.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
    
#CAMBIO DE CONTRASEÑA
class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'passwordCambio.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'passwordExitoso.html', {})

#CREACIÓN LIBRO
class LibroCreacion(LoginRequiredMixin, CreateView):
    model = Libro
    form_class = FormularioNuevoLibro
    success_url = reverse_lazy('home')
    template_name = 'libroCreacion.html'

    def form_valid(self, form):
        if form.is_valid():   
            form.instance.usuario = self.request.user
            return super(LibroCreacion, self).form_valid(form)
        else:
        # Imprimir los errores del formulario en el servidor
            print(form.errors)  # Esto te mostrará los errores de validación en la consola
            return self.form_invalid(form)







#CIENCIA FICCIÓN
class Ciencia_ficciónLista(LoginRequiredMixin, ListView):
    model = Libro
    context_object_name = 'ciencia_ficción'
    template_name = 'listaCiencia_ficción.html'
    login_url = '/login/'
    def get_queryset(self):
        return Libro.objects.filter(libro='ciencia_ficción') # Filtramos los libros de Ciencia Ficción

class Ciencia_ficciónDetalle(LoginRequiredMixin, DetailView):
    model = Libro
    context_object_name = 'ciencia_ficción'
    template_name = 'Ciencia_ficciónDetalle.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregar los comentarios al contexto
        context['comentarios'] = self.object.comentarios.all()
        return context

class Ciencia_ficciónUpdate(LoginRequiredMixin, UpdateView):
    model = Libro
    form_class = ActualizacionLibro
    success_url = reverse_lazy('Ciencia_ficción')
    context_object_name = 'ciencia_ficción'
    template_name = 'Ciencia_ficciónEdicion.html'

class Ciencia_ficciónDelete(LoginRequiredMixin, DeleteView):
    model = Libro
    success_url = reverse_lazy('Ciencia_ficción')
    context_object_name = 'ciencia_ficción'
    template_name = 'Ciencia_ficciónBorrado.html'

#NOVELAS

class NovelasLista(LoginRequiredMixin, ListView):
    model = Libro
    context_object_name = 'novelas'
    template_name = 'listanovelas.html'
    login_url = '/login/'
    def get_queryset(self):
        return Libro.objects.filter(libro='novelas') # Filtramos los libros de Ciencia Ficción

class NovelasDetalle(LoginRequiredMixin, DetailView):
    model = Libro
    context_object_name = 'novelas'
    template_name = 'novelasDetalle.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregar los comentarios al contexto
        context['comentarios'] = self.object.comentarios.all()
        return context

class NovelasUpdate(LoginRequiredMixin, UpdateView):
    model = Libro
    form_class = ActualizacionLibro
    success_url = reverse_lazy('novelas')
    context_object_name = 'novelas'
    template_name = 'novelasEdicion.html'

class NovelasDelete(LoginRequiredMixin, DeleteView):
    model = Libro
    success_url = reverse_lazy('novelas')
    context_object_name = 'novelas'
    template_name = 'novelasBorrado.html'

#AUTOAYUDA
class AutoayudaLista(LoginRequiredMixin, ListView):
    model = Libro
    context_object_name = 'autoayuda'
    template_name = 'listaautoayuda.html'
    login_url = '/login/'
    def get_queryset(self):
        return Libro.objects.filter(libro='autoayuda') # Filtramos los libros de Ciencia Ficción

class AutoayudaDetalle(LoginRequiredMixin, DetailView):
    model = Libro
    context_object_name = 'autoayuda'
    template_name = 'autoayudaDetalle.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregar los comentarios al contexto
        context['comentarios'] = self.object.comentarios.all()
        return context

class AutoayudaUpdate(LoginRequiredMixin, UpdateView):
    model = Libro
    form_class = ActualizacionLibro
    success_url = reverse_lazy('autoayuda')
    context_object_name = 'autoayuda'
    template_name = 'autoayudaEdicion.html'

class AutoayudaDelete(LoginRequiredMixin, DeleteView):
    model = Libro
    success_url = reverse_lazy('autoayuda')
    context_object_name = 'autoayuda'
    template_name = 'autoayudaBorrado.html'

#TERROR
class TerrorLista(LoginRequiredMixin, ListView):
    model = Libro
    context_object_name = 'terror'
    template_name = 'listaterror.html'
    login_url = '/login/'
    def get_queryset(self):
        return Libro.objects.filter(libro='terror') # Filtramos los libros de Ciencia Ficción

class TerrorDetalle(LoginRequiredMixin, DetailView):
    model = Libro
    context_object_name = 'terror'
    template_name = 'terrorDetalle.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregar los comentarios al contexto
        context['comentarios'] = self.object.comentarios.all()
        return context

class TerrorUpdate(LoginRequiredMixin, UpdateView):
    model = Libro
    form_class = ActualizacionLibro
    success_url = reverse_lazy('terror')
    context_object_name = 'terror'
    template_name = 'terrorEdicion.html'

class TerrorDelete(LoginRequiredMixin, DeleteView):
    model = Libro
    success_url = reverse_lazy('terror')
    context_object_name = 'terror'
    template_name = 'terrorBorrado.html'


# COMENTARIOS

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'comentario.html'
    def get_success_url(self):
        # Redirigir al detalle del libro después de agregar el comentario
        return reverse_lazy('Ciencia_ficción_detalle', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        # Asociar el comentario con el libro
        libro = get_object_or_404(Libro, pk=self.kwargs['pk'])
        form.instance.comentario = libro
        return super().form_valid(form)



def aboutME(request):
    return render(request, 'aboutME.html', {})
