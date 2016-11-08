from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Plato(models.Model):
    imagen = models.ImageField(upload_to='photo/',null=True,blank=True)
    titulo = models.CharField(max_length=20)
    descripcion = models.TextField()
    sector_zona = models.CharField(max_length=20)
    ingrediente = models.TextField()
    cal_gras_trans = models.TextField()
    costo = models.IntegerField()



class Compra(models.Model):
    usuario = models.ForeignKey(User, null=True,blank=True)
    plato = models.ForeignKey(Plato, null=True,blank=True)


class Corazon(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True)
    plato = models.ForeignKey(Plato, null=True, blank=True)


class Red(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True)
    plato = models.ForeignKey(Plato, null=True, blank=True)