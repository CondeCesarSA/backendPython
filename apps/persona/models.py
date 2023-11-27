from django.db import models


class Pais(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre

class Provincia(models.Model):
    nombre = models.CharField(max_length=255)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name="provincia")
    def __str__(self):
        return f"{self.nombre} ({self.pais})"

class Localidad(models.Model):
    nombre = models.CharField(max_length=255)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, related_name="localidad")

    def __str__(self):
        return f"{self.nombre} ({self.provincia})"

class Direccion(models.Model):
    calle = models.CharField(max_length=255)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE, related_name="direccion")

    def __str__(self):
        return f"{self.calle}, {self.localidad}"

class Telefono(models.Model):
    codArea = models.IntegerField()
    prefijo = models.IntegerField()
    numero = models.IntegerField()

    def __str__(self):
        return f"{self.codArea}-{self.prefijo}-{self.numero}"

class Persona(models.Model):
    apellido = models.CharField(max_length=255)
    dni = models.IntegerField()
    fechaNacimiento = models.DateField()
    nacionalidad = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name="nacionalidad")
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, related_name="direccion")
    telefono = models.ForeignKey(Telefono, on_delete=models.CASCADE, related_name="telefono")

    def __str__(self):
        return f"{self.apellido}, DNI: {self.dni}, Nac.: {self.nacionalidad}, Dir.: {self.direccion}, Tel.: {self.telefono}"
