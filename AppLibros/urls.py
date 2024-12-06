from django.urls import path
from AppLibros import views
from .views import LibroCreacion,Ciencia_ficciónLista,Ciencia_ficciónDetalle, Ciencia_ficciónUpdate,Ciencia_ficciónDelete,LoginPagina, RegistroPagina, UsuarioEdicion, CambioPassword, HomeView,ComentarioPagina
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),

    path('login/',views.LoginPagina.as_view(),name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.RegistroPagina.as_view(), name='registro'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),
    path('Novelas/',views.Novelas,name='Novelas'),
    path('Terror/',views.Terror,name='Terror'),
    path('Autoayuda/',views.Autoayuda,name='Autoayuda'),

    path('listaCiencia_ficción/', Ciencia_ficciónLista.as_view(), name='Ciencia_ficción'),
    

    path('Ciencia_ficciónDetalle/<int:pk>/', Ciencia_ficciónDetalle.as_view(), name='Ciencia_ficción_detalle'),
    

    path('Ciencia_ficciónEdicion/<int:pk>/', Ciencia_ficciónUpdate.as_view(), name='Ciencia_ficción_editar'),
    


    path('Ciencia_ficciónBorrado/<int:pk>/', Ciencia_ficciónDelete.as_view(), name='Ciencia_ficción_eliminar'),
   
    #comentario
    path('ciencia_ficciónDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),

    #creacion
    path('libroCreacion/', LibroCreacion.as_view(), name='Publicar'),

    
]