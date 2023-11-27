from django.test import TestCase
from datetime import date
from apps.user.models import User, Tarjeta
from apps.persona.models import Pais, Direccion, Localidad, Provincia

class UserModelTest(TestCase):
    def setUp(self):
        # Crear instancias necesarias para las pruebas
        pais = Pais.objects.create(nombre="Argentina")
        provincia = Provincia.objects.create(nombre="Buenos Aires", pais=pais)
        localidad = Localidad.objects.create(nombre="La Plata", provincia=provincia)
        direccion = Direccion.objects.create(calle="Calle 123", localidad=localidad)
        tarjeta = Tarjeta.objects.create(BancoEmisor="banco1", TipoTarjeta="tipo1")

        # Crear un usuario para las pruebas
        self.user = User.objects.create(
            nombre="Juan",
            apellido="Perez",
            dni=12345678,
            fechaNacimiento=date(1990, 1, 1),
            nacionalidad=pais,
            direccion=direccion,
            telefono=None,  # Puedes ajustar según tus necesidades
            Tarjeta=tarjeta,
            Registrado=date.today()
        )

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)

    def test_user_attributes(self):
        self.assertEqual(self.user.nombre, "Juan")
        self.assertEqual(self.user.apellido, "Perez")
        # Agrega más aserciones según los atributos que quieras probar

    def test_user_str_representation(self):
        self.assertEqual(
            str(self.user),
            "Juan Perez, DNI: 12345678"
        )

    def test_user_has_tarjeta(self):
        self.assertEqual(self.user.Tarjeta.BancoEmisor, "banco1")
        self.assertEqual(self.user.Tarjeta.TipoTarjeta, "tipo1")
