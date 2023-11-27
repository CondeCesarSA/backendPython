from django.db import models
from apps.persona.models import Persona

class Banco(models.Model):
    NACION_ARGENTINA = 'BNA'
    MACRO = 'Macro'
    GALICIA = 'Galicia'
    SANTANDER_RIO = 'Santander Rio'
    BBVA_ARGENTINA = 'BBVA Argentina'
    HIPOTECARIO = 'Hipotecario'
    CIUDAD = 'Ciudad'
    ITAU_ARGENTINA = 'Itau Argentina'
    PATAGONIA = 'Patagonia'
    COLUMBIA = 'Columbia'

    BANCOS_CHOICES = [
        (NACION_ARGENTINA, 'Banco de la Nación Argentina (BNA)'),
        (MACRO, 'Banco Macro'),
        (GALICIA, 'Banco Galicia'),
        (SANTANDER_RIO, 'Banco Santander Río'),
        (BBVA_ARGENTINA, 'Banco BBVA Argentina'),
        (HIPOTECARIO, 'Banco Hipotecario'),
        (CIUDAD, 'Banco Ciudad'),
        (ITAU_ARGENTINA, 'Banco Itaú Argentina'),
        (PATAGONIA, 'Banco Patagonia'),
        (COLUMBIA, 'Banco Columbia'),
    ]

    banco = models.CharField(max_length=20, choices=BANCOS_CHOICES)

    def __str__(self):
        return self.get_banco_display()

class TipoTarjeta(models.TextChoices):
    VISA = 'Visa', 
    MASTERCARD = 'MasterCard', 
    AMERICAN_EXPRESS = 'American Express', 
    TARJETA_NARANJA = 'Tarjeta Naranja', 
    TARJETA_SHOPPING = 'Tarjeta Shopping',
    CABAL = 'Cabal', 
    MAESTRO = 'Maestro',
    ARGENCARD = 'Argencard'

class Tarjeta(models.Model):
    banco_emisor  = models.ForeignKey(Banco, on_delete=models.CASCADE)
    tipo_tarjeta  = models.CharField(max_length=20, choices=TipoTarjeta.choices)

class User(Persona):
    tarjeta  = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)
    registrado  = models.DateField()
