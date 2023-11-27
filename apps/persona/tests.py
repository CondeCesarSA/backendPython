from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Pais, Provincia, Localidad, Direccion, Telefono, Persona
from datetime import date

class PersonaModelTest(TestCase):
    def setUp(self):
        # Crear instancias de los modelos para usar en las pruebas
        self.pais = Pais.objects.create(nombre="Argentina")
        self.provincia = Provincia.objects.create(nombre="Buenos Aires", pais=self.pais)
        self.localidad = Localidad.objects.create(nombre="La Plata", provincia=self.provincia)
        self.direccion = Direccion.objects.create(calle="Calle 123", localidad=self.localidad)
        self.telefono = Telefono.objects.create(codArea=11, prefijo=123, numero=4567890)
        self.persona = Persona.objects.create(
            nombre="Juan",
            apellido="Perez",
            dni=12345678,
            fechaNacimiento=date(1990, 1, 1),
            nacionalidad=self.pais,
            direccion=self.direccion,
            telefono=self.telefono
        )

    def test_pais_model(self):
        self.assertEqual(str(self.pais), "Argentina")

    def test_provincia_model(self):
        self.assertEqual(str(self.provincia), "Buenos Aires")

    def test_localidad_model(self):
        self.assertEqual(str(self.localidad), "La Plata")

    def test_direccion_model(self):
        self.assertEqual(str(self.direccion), "Calle 123, La Plata, Buenos Aires, Argentina")

    def test_telefono_model(self):
        self.assertEqual(str(self.telefono), "+11 123 4567890")

    def test_persona_model(self):
        self.assertEqual(str(self.persona), "Juan Perez, DNI: 12345678")

    def test_persona_fecha_nacimiento(self):
        self.assertEqual(self.persona.fechaNacimiento, date(1990, 1, 1))
