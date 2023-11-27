# admin.py
from django.contrib import admin
from apps.user.models import Banco, TipoTarjeta, Tarjeta, User

# @admin.register(Banco)
# class BancoAdmin(admin.ModelAdmin):
#     list_display = ('banco',)

# @admin.register(TipoTarjeta)
# class TipoTarjetaAdmin(admin.ModelAdmin):
#     list_display = ('tipo_tarjeta',)

@admin.register(Tarjeta)
class TarjetaAdmin(admin.ModelAdmin):
    list_display = ('banco_emisor', 'tipo_tarjeta',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'dni', 'fechaNacimiento', 'nacionalidad', 'direccion', 'telefono', 'tarjeta', 'registrado',)
