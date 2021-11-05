from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True, verbose_name='Estado')
    fc = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    fm = models.DateTimeField(auto_now=True, verbose_name='Modificado')
    uc = models.ForeignKey(User, on_delete=models.CASCADE)
    um = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True
