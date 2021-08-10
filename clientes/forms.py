
""" Formularios Clientes."""

# Django
from django import forms

# Models
from django.contrib.auth.models import User
from clientes.models import Cliente
from bancos.models import Banco


import pdb



class CreateForm(forms.Form):
    """Formulario creación clientes."""
    
    banco = forms.ModelChoiceField(queryset=Banco.objects.all())
    nombre = forms.CharField(min_length=2, max_length=50, label='Nombre')
    apellido = forms.CharField(min_length=2, max_length=50, label='Apellido')

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput(),
        
    )

    # Validacion adicional sobreescribiendo clean_fieldName() Method
    def clean_username(self): # Validacion de Email
        """Email debe ser único."""
        email = self.cleaned_data['email']
        email_taken = Cliente.objects.filter(email=email).exists()
       
        if email_taken:
            raise forms.ValidationError('Email está en uso.') # Lanzamos una excepcion que eleva el error hasta el nivel de html
        return email


    def save(self): # Metodo para crear el usuario si el form es valido
        """Crear usuario."""
        data = self.cleaned_data        
        cliente = Cliente.objects.create(**data)
        cliente.save()



class ClientForm(forms.Form):
    # Form para informacion de clientes.

    # Fixed choice fields
    TIPO_PERSONA = (
         ('Natural', 'Natural'),
         ('Juridico', 'Juridico'),
    )

    
    nombre = forms.CharField(min_length=2, max_length=50)
    apellido = forms.CharField(min_length=2, max_length=50)
    telefono = forms.CharField(max_length=20, required=False)
    
    edad = forms.CharField(min_length=2, max_length=50, required=False)
    direccion_habitacion = forms.CharField(max_length=30, required=False)
    

    