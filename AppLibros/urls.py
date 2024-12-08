from django.urls import path
from AppLibros import views
from .views import LibroCreacion,Ciencia_ficciónLista,NovelasLista,AutoayudaLista,TerrorLista,Ciencia_ficciónDetalle,NovelasDetalle,AutoayudaDetalle,TerrorDetalle, Ciencia_ficciónUpdate,NovelasUpdate,AutoayudaUpdate,TerrorUpdate,Ciencia_ficciónDelete,NovelasDelete,AutoayudaDelete,TerrorDelete,aboutME, RegistroPagina, UsuarioEdicion, CambioPassword,LoginPagina, HomeView,ComentarioPagina
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
    
    

    path('listaCiencia_ficción/', Ciencia_ficciónLista.as_view(), name='Ciencia_ficción'),
    path('listanovelas/', NovelasLista.as_view(), name='novelas'),
    path('listaautoayuda/', AutoayudaLista.as_view(), name='autoayuda'),
    path('listaterror/', TerrorLista.as_view(), name='terror'),


    path('Ciencia_ficciónDetalle/<int:pk>/', Ciencia_ficciónDetalle.as_view(), name='Ciencia_ficción_detalle'),
    path('novelasDetalle/<int:pk>/', NovelasDetalle.as_view(), name='novelas_detalle'),
    path('autoayudaDetalle/<int:pk>/', AutoayudaDetalle.as_view(), name='autoayuda_detalle'),
    path('terrorDetalle/<int:pk>/', TerrorDetalle.as_view(), name='terror_detalle'),


    path('Ciencia_ficciónEdicion/<int:pk>/', Ciencia_ficciónUpdate.as_view(), name='Ciencia_ficción_editar'),
    path('novelasEdicion/<int:pk>/', NovelasUpdate.as_view(), name='novelas_editar'),
    path('autoayudaEdicion/<int:pk>/', AutoayudaUpdate.as_view(), name='autoayuda_editar'),
    path('terrorEdicion/<int:pk>/', TerrorUpdate.as_view(), name='terror_editar'),



    path('Ciencia_ficciónBorrado/<int:pk>/', Ciencia_ficciónDelete.as_view(), name='Ciencia_ficción_eliminar'),
    path('novelasBorrado/<int:pk>/', NovelasDelete.as_view(), name='novelas_eliminar'),
    path('autoayudaBorrado/<int:pk>/', AutoayudaDelete.as_view(), name='autoayuda_eliminar'),
    path('terrorBorrado/<int:pk>/', TerrorDelete.as_view(), name='terror_eliminar'),

    #comentario
    path('ciencia_ficciónDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('novelasDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('autoayudaDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('terrorDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),

    #creacion
    path('libroCreacion/', LibroCreacion.as_view(), name='Publicar'),
    path('acercademí/', views.aboutME, name='aboutME'),
    
]