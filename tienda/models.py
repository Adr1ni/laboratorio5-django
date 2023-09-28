from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')

    def __str__(self):
        return self.nombre
    

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6,decimal_places=2)
    stock = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date_published')

    def __str__(self):
        return self.nombre
    

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    telefono = models.CharField(max_length=9, unique=True)
    direccion = models.TextField(null=False)
    email = models.EmailField(null=False, unique=True)
    fecha_de_nacimiento = models.DateField()
    history = HistoricalRecords()

    def __str__(self):
        return self.nombre + ' ' + self.apellidos
