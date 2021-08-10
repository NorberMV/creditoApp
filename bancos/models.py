"""Modelo de Bancos."""

from django.db import models

# Create your models here.
class Banco(models.Model):
    """ Modelo de entidades Bancarias. """


    # Fixed choice fields
    TIPO_BANCO = (
         ('Privado', 'Privado'),
         ('Gobierno', 'Gobierno'),
    )

    nombre = models.CharField(max_length=20, blank=True)
    tipo = models.CharField(max_length=20, choices=TIPO_BANCO, null=True)
    direccion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        """ Retorna el nombre 
        del banco."""

        return self.nombre