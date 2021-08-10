
from django.contrib import admin

# Models
from clientes.models import Cliente
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Cliente)
#admin.site.register(Product)