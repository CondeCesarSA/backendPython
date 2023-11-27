from django.db import models

class Pais(models.Model):
    
    nombre = models.CharField(max_length=255)

class Provincia(models.Model):
    nombre = models.CharField(max_length=255)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name="provincia")

class Localidad(models.Model):
    nombre = models.CharField(max_length=255)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE
                                  , related_name="localidad")

class Direccion(models.Model):
    calle = models.CharField(max_length=255)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE,
                                  related_name="direccion")

class Telefono(models.Model):
    codArea = models.IntegerField()
    prefijo = models.IntegerField()
    numero = models.IntegerField()

class Persona(models.Model):
    apellido = models.CharField(max_length=255)
    dni = models.IntegerField()
    fechaNacimiento = models.DateField()
    nacionalidad = models.ForeignKey(Pais,
                                      on_delete=models.CASCADE,
                                        related_name="nacionalidad")
    direccion = models.ForeignKey(Direccion,
                                   on_delete=models.CASCADE,
                                   related_name="direccion")
    telefono = models.ForeignKey(Telefono, on_delete=models.CASCADE
                                 ,related_name="telefono")
