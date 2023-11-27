from django.db import models
from apps.user.models import User

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    cuit = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Factura(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='user')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='facturas')
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Factura #{self.id}"
