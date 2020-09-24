from django.test import TestCase
from .models import Disease


class DiseaseTest(TestCase):
    def setUp(self):
        Disease.objects.create(name="Prueba 1")

    def test001_a_diseases_has_a_name(self):
        prueba = Disease.objects.get(name="Prueba 1")
        self.assertEqual(prueba.name, "Prueba 1")
