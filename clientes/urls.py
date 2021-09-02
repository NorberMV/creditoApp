""" Manejo de Clientes URLs."""

# Django
from django.urls import path

# View
from clientes import views


urlpatterns = [

    
    # Manejo de clientes
    
    path(                                         # Creación de clientes
        route='crear-clientes/',
        view=views.crear_cliente,
        name='crear-clientes'
    ),

    path(                                          # Lista los clientes
        route='lista-clientes/',
        view=views.ListaClientes.as_view(),
        name='lista-clientes',
    ),

    path(                                         # Actualización de datos de cliente
        route='actualizar-clientes/<int:client_id>/',
        view=views.actualizar_cliente,
        name='actualizar-clientes',
    ),

    path(
        route='detalle-clientes/<int:client_id>/',
        view=views.detalle_cliente,
        name='detalle-clientes'
    ),

    path(
        route='eliminar-clientes/<int:client_id>/',
        view=views.eliminar_cliente,
        name='eliminar-clientes'
    ),
    # FUNCION DE PRUEBA
    path(
        route='prueba/',
        view=views.prueba_function,
        name='prueba'
    )



]