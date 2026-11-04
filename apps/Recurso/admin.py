from django.contrib import admin
from .models import Recurso

@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'disponibilidad')