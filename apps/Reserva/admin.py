from django.contrib import admin
from .models import Reserva


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('docente_responsable', 'materia', 'curso', 'fecha_reserva', 'fecha_prestamo', 'hora_prestamo')