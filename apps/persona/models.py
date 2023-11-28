from django.db import models


class Pais(models.Model):
    nombre = models.CharField(max_length=255, default="Argentina")

    def __str__(self):
        return self.nombre

class Provincia(models.Model):
    PROVINCIAS_CHOICES = [
        ("Buenos Aires", "Buenos Aires"),
        ("Córdoba", "Córdoba"),
        ("Santa Fe", "Santa Fe"),
        ("Mendoza", "Mendoza"),
        ("Salta", "Salta"),
    ]

    nombre = models.CharField(max_length=255, choices=PROVINCIAS_CHOICES)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name="provincias")

    def __str__(self):
        return f"{self.nombre} ({self.pais})"

class Localidad(models.Model):
    LOCALIDADES_BUENOS_AIRES_CHOICES = [
        ("Ciudad Autónoma de Buenos Aires", "Ciudad Autónoma de Buenos Aires"),
        ("La Plata", "La Plata"),
        ("Mar del Plata", "Mar del Plata"),
        ("Quilmes", "Quilmes"),
        ("San Isidro", "San Isidro"),
    ]

    LOCALIDADES_CORDOBA_CHOICES = [
        ("Córdoba", "Córdoba"),
        ("Villa María", "Villa María"),
        ("Río Cuarto", "Río Cuarto"),
        ("Alta Gracia", "Alta Gracia"),
        ("Jesús María", "Jesús María"),
    ]

    LOCALIDADES_SANTA_FE_CHOICES = [
        ("Santa Fe", "Santa Fe"),
        ("Rosario", "Rosario"),
        ("Santo Tomé", "Santo Tomé"),
        ("Venado Tuerto", "Venado Tuerto"),
        ("Rafaela", "Rafaela"),
    ]

    LOCALIDADES_MENDOZA_CHOICES = [
        ("Mendoza", "Mendoza"),
        ("San Rafael", "San Rafael"),
        ("Godoy Cruz", "Godoy Cruz"),
        ("Maipú", "Maipú"),
        ("Luján de Cuyo", "Luján de Cuyo"),
    ]

    LOCALIDADES_SALTA_CHOICES = [
        ("Salta", "Salta"),
        ("San Ramón de la Nueva Orán", "San Ramón de la Nueva Orán"),
        ("Tartagal", "Tartagal"),
        ("Joaquín V. González", "Joaquín V. González"),
        ("Metán", "Metán"),
    ]

    nombre = models.CharField(max_length=255, choices=LOCALIDADES_BUENOS_AIRES_CHOICES + LOCALIDADES_CORDOBA_CHOICES +
                                                  LOCALIDADES_SANTA_FE_CHOICES + LOCALIDADES_MENDOZA_CHOICES +
                                                  LOCALIDADES_SALTA_CHOICES)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, related_name="localidades")

    def __str__(self):
        return f"{self.nombre} ({self.provincia})"


class Direccion(models.Model):
    calle = models.CharField(max_length=255, null=True, blank=True)
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
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    dni = models.IntegerField()
    fecha_nacimiento = models.DateField(null=True, blank=True)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name="pais")
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, related_name="direccion")
    telefono = models.OneToOneField(Telefono, on_delete=models.CASCADE, related_name="telefono", null=True, blank=True)

def __str__(self):
    pais_str = f"Nac.: {self.nacionalidad}" if self.nacionalidad else "Nac.: (sin asignar)"
    direccion_str = f"Dir.: {self.direccion}" if self.direccion else "Dir.: (sin asignar)"
    telefono_str = f"Tel.: {self.telefono}" if self.telefono else "Tel.: (sin asignar)"

    return f"Nombre: {self.nombre}, Apellido: {self.apellido}, DNI: {self.dni}, {pais_str}, {direccion_str}, {telefono_str}"
