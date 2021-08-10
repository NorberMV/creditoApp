
"""Modelo de Clientes."""

# Django depedencies
from django.contrib.auth.models import User
from django.db import models

# Modelos
from bancos.models import Banco

# Create your models here.



class Cliente(models.Model):
    """Modelo de Clientes. """

    # Fixed choice fields
    TIPO_PERSONA = (
         ('Natural', 'Natural'),
         ('Juridico', 'Juridico'),
    )

    banco = models.ForeignKey(Banco, on_delete=models.CASCADE, blank=True, null=True)
    nombre = models.CharField(max_length=200, null=True)
    apellido = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    fecha_nacimiento = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    edad = models.IntegerField(default=0, null=True, blank=True)
    nacionalidad = models.CharField(max_length=200, blank=True)
    direccion_habitacion = models.CharField(max_length=200, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    tipo_persona = models.CharField(max_length=20, choices=TIPO_PERSONA, null=True)

    """ Método para retornar nombre completo del Cliente
        para usarlo como propiedad de la clase Cliente. """
    @property 
    def nombre_completo(self):           
        nombre_completo = '{} {}'.format(self.nombre, self.apellido)
        return nombre_completo

    def __str__(self):
        """retorna nombre completo."""
        return self.nombre_completo
