

# Register your models here.
# admin.py
from django.contrib import admin
from apps.persona.models import Pais, Provincia, Localidad, Direccion, Telefono, Persona

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais',)

@admin.register(Localidad)
class LocalidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'provincia',)

@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('calle', 'localidad',)

@admin.register(Telefono)
class TelefonoAdmin(admin.ModelAdmin):
    list_display = ('codArea', 'prefijo', 'numero',)

# Asegúrate de que la clase Persona también esté registrada en el admin si no lo has hecho ya
@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'dni', 'fechaNacimiento', 'nacionalidad', 'direccion', 'telefono',)
