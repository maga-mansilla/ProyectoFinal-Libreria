from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Libro(models.Model):
    libroSeleccion = (
    ('ciencia_ficción','Ciencia_Ficción'),
    ('novelas', 'Novelas'),
    ('autoayuda','Autoayuda'),
    ('terror','Terror'),
    ('otro','Otro'),
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    libro = models.CharField(max_length=15, choices=libroSeleccion, default='autoayuda')
    escritor = models.CharField(max_length=40)
    editorial = models.CharField(max_length=40)
    descripcion = models.TextField(null=True, blank=True)
    cantidad_de_paginas= models.IntegerField()
    year = models.IntegerField() 
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    telefonoContacto = models.IntegerField()
    emailContacto = models.EmailField()
    imagenLibro = models.ImageField(null=True, blank=True, upload_to="imagenes/")
    

    class Meta:
        ordering = ['usuario', '-fechaPublicacion']

    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
        comentario = models.ForeignKey(Libro, related_name='comentarios', on_delete=models.CASCADE, null=True)
        nombre = models.CharField(max_length=40)
        mensaje = models.TextField(null=True, blank=True)
        fechaComentario = models.DateTimeField(auto_now_add=True)

        class Meta:
            ordering = ['-fechaComentario']

        def __str__(self):
            return '%s - %s' % (self.nombre, self.comentario)
