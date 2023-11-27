from django.db import models
from apps.factura.models import Factura
from apps.producto.models import Component
class Detalle(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Component, on_delete=models.CASCADE , related_name= 'componentes')

    def __str__(self):
        return f"Detalle de la Factura #{self.factura.id}"