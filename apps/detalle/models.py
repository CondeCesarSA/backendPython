from django.db import models
from apps.factura.models import Factura
from apps.producto.models import Component
class Detalle(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name='factura')
    producto = models.ForeignKey(Component, on_delete=models.CASCADE , related_name= 'producto')

    def __str__(self):
        return f"Detalle de la Factura #{self.factura.id}"