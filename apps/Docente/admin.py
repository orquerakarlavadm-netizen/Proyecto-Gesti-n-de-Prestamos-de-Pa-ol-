from django.contrib import admin
from .models import Docente

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('dni', 'nombre', 'apellido', 'mail')