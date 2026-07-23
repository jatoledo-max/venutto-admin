from django.db import models

class Categoria(models.Model):
    nombre= models.CharField(max_length=50)
    disponible=models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Meta:
    verbose_name = "Categoría"
    verbose_name_plural = "Categorías"

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.DecimalField(max_digits=8, decimal_places=2)
    descripcion=models.TextField()
    categoria=models.ForeignKey(Categoria,
    on_delete=models.PROTECT)
    disponible=models.BooleanField(default=True)

    def __str__(self):
        return self.nombre