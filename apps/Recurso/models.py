from django.db import models

class Recurso(models.Model):
    tipo = models.CharField(max_length=100)
    disponibilidad = models.BooleanField(default=True)

    def __str__(self):
        return self.tipo