from django.db import models

from apps.Docente.models import Docente
from apps.Materia.models import Materia
from apps.Curso.models import Curso
from apps.Recurso.models import Recurso

class Reserva(models.Model):
    docente_responsable = models.ForeignKey(Docente, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    
    recursos = models.ManyToManyField(Recurso)
    
    fecha_reserva = models.DateField(auto_now_add=True)
    fecha_prestamo = models.DateField()
    hora_prestamo = models.CharField(max_length=20)
    
    motivo = models.CharField(max_length=250) 

    def __str__(self):
        return f"Reserva {self.fecha_prestamo} - {self.docente_responsable}"