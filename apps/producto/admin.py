from django.contrib import admin
from apps.producto.models import Manufacturer, Physical, Dimensions, UnitResistance, UnitVolt, UnitCapacitance, Technical, Distributor, Component

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Physical)
class PhysicalAdmin(admin.ModelAdmin):
    list_display = ('package', 'mount', 'number_of_pins')

@admin.register(Dimensions)
class DimensionsAdmin(admin.ModelAdmin):
    list_display = ('length', 'width', 'height', 'depth')

@admin.register(UnitResistance)
class UnitResistanceAdmin(admin.ModelAdmin):
    list_display = ('value', 'unit')

@admin.register(UnitVolt)
class UnitVoltAdmin(admin.ModelAdmin):
    list_display = ('voltage', 'unit')

@admin.register(UnitCapacitance)
class UnitCapacitanceAdmin(admin.ModelAdmin):
    list_display = ('value', 'unit')

@admin.register(Technical)
class TechnicalAdmin(admin.ModelAdmin):
    list_display = ('pines', 'resistance', 'capacitance', 'voltage')

@admin.register(Distributor)
class DistributorAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'moq', 'technical', 'dimensions', 'physical', 'manufacturer', 'distributor')
