from django.db import models

class Curso(models.Model):
    anio = models.CharField(max_length=50)
    division = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.anio} {self.division}"