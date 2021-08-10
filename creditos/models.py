"""Modelo de Créditos."""

from django.db import models
from clientes.models import *
from bancos.models import Banco

import pdb

# Create your models here.

class Credito(models.Model):
    """Modelo de Creditos."""
    
    # Fixed choice fields

    TIPO_CREDITOS = (
         ('Automotriz', 'Automotriz'),
         ('Hipotecarios', 'Hipotecarios'),
         ('Comerciales', 'Comerciales'),    
    )

    
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE, blank=True, null=True) # Lista de Selección bancos en la base de datos
    descripcion_credito = models.TextField(blank=True)
    pago_minimo = models.DecimalField(max_digits=10, decimal_places=2) # Número real con dos decimales
    pago_maximo = models.DecimalField(max_digits=10, decimal_places=2) # Número real con dos decimales
    plazo_credito = models.IntegerField(default=0, null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now=True)
    tipo_credito = models.CharField(max_length=20, choices=TIPO_CREDITOS, null=True) # Lista de Selección: Automotriz, Hipotecarios y Comerciales

    def __str__(self):
        """Retorna tipo de crédito y cliente."""
        return 'Credito {} de @{}'.format(self.tipo_credito, self.cliente.nombre)