"""Vistas de Clientes."""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, FormView, UpdateView, ListView
from django.urls import reverse

# Models
from django.contrib.auth.models import User
from clientes.models import Cliente

# Forms
from clientes.forms import CreateForm, ClientForm

# Utilities
import pdb




def crear_cliente(request):
    
    """ Vista creación cliente. """

    if request.method == 'POST':                       # Recibo del formulario
        form = CreateForm(request.POST)
        if form.is_valid():                            # Si el formulario es válido == True
            form.save()                                # Guardamos el cliente
            return redirect('clientes:crear-clientes') # Usuario creado exitosamente
    else:
        form = CreateForm()                            # Si el request no es POST, enviamos formulario vacío
        

    return render(
        request=request,
        template_name='clientes/crear_cliente.html',
        context={
            'form': form,
            }
    )
    



def detalle_cliente(request, **kwarg):                 
    
    """ Vista información detalle cliente creado
        exitosamente."""

    
    client_id = kwarg['client_id']               # Tomamos el valor kwarg del id del cliente tomado de la URL
    cliente = Cliente.objects.get(id=client_id)  # creamos el objeto Cliente especificado filtrado por su id    
    mensaje = 'Cliente actualizado exitosamente!'

    return render(
        request=request,
        template_name='clientes/actualizar.html',
        context={
            'cliente': cliente,
            'mensaje': mensaje,
        }
    )
    


def actualizar_cliente(request, **kwarg):           

    """ Vista de actualización de usuario. """
    #pdb.set_trace()
    client_id = kwarg['client_id']

    if request.method =='POST':
        form = ClientForm(request.POST)
        #pdb.set_trace()
        if form.is_valid():
            
            data = form.cleaned_data
            cliente = Cliente.objects.get(id=client_id)

            # Actualizamos información del cliente
            cliente.nombre = data['nombre']
            cliente.apellido = data['apellido']
            cliente.direccion_habitacion = data['direccion_habitacion']
            cliente.edad = data['edad']
            cliente.telefono = data['telefono']
            cliente.save()                                               # Guarda la nueva información del cliente

            url = reverse('clientes:detalle-clientes',kwargs={'client_id':cliente.id}) 
            return redirect(url)
    else:
        form = ClientForm()
        cliente = Cliente.objects.get(id=client_id)
        

    return render(
        request=request,
        template_name='clientes/actualizar.html',
        context={
            'cliente': cliente,
            'form': form,
        }
    )




class ListaClientes(ListView):

    """Vista retorna todos los clientes existentes 
        en la base de datos."""

    template_name = 'clientes/lista_clientes.html'
    model = Cliente                  # Cargamos el modelo Cliente
    #pdb.set_trace()
    ordering = ('id',)               # Ordena los usuarios por 'id' en el template
    context_object_name = 'clientes' # Envía como contexto el Objeto Cliente
    



def eliminar_cliente(request,**kwarg):

    """ Vista de eliminación de usuario. """

    client_id = kwarg['client_id']
    cliente = Cliente.objects.get(id = client_id)
    
    cliente.delete()
    
    url = reverse('clientes:lista-clientes') 
    
    return redirect(url)


def prueba_function(request):
    clientes = Cliente.objects.all()
    
    return render(
        request=request,
        template_name='clientes/prueba.html/',
        context = {
            'clientes':clientes,
            #'mensaje': mensaje,
        }
    )