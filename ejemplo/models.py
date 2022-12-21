from django.db import models


# Create your models here.
from django.db import models
class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    def __str__(self):
      return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"

from django.db import models
class Obreros(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    edad = models.IntegerField()
    def __str__(self):
      return f"{self.nombre},{self.categoria} {self.edad}, {self.id}"

from django.db import models
class Obras(models.Model):
    nombre = models.CharField(max_length=50)
    direccion= models.CharField(max_length=100)
    niveles = models.IntegerField()
    def __str__(self):
      return f"{self.nombre},{self.direccion} {self.niveles}, {self.id}"
      