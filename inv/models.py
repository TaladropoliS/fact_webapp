from django.db import models
from base.models import ClaseModelo


class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Categoría',
        verbose_name='Descripción',
        unique=True
    )

    def __str__(self):
        return f'{self.descripcion}'

    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['fc']
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'


class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la SubCategoría',
        verbose_name='SubDescripción'
    )

    def __str__(self):
        return f'{self.categoria.descripcion} : {self.descripcion}'

    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['fc']
        verbose_name = 'SubCategoría'
        verbose_name_plural = 'SubCategorías'
        unique_together = ('categoria', 'descripcion')
