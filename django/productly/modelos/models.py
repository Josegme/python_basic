from django.db import models

class Categoria(models.Model): 
    nombre = models.CharField(max_length=255) #cadena de texto limitada

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    nombre = models.IntegerField()
    puntaje = models.FloatField()
    #cascade
    #protect
    #restrict
    #set_null
    #set_default
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE
        ) #relacion entre Categoria y Producto

