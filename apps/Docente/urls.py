from django.urls import path
from .views import (DocenteListView, DocenteDetailView, DocenteCreateView, DocenteUpdateView, DocenteDeleteView)

app_name = "docente"

urlpatterns = [
    path("", DocenteListView.as_view(), name="docente_list"),
    path("nuevo/", DocenteCreateView.as_view(), name="docente_create"),
    path("<int:pk>/", DocenteDetailView.as_view(), name="docente_detail"),
    path("<int:pk>/editar/", DocenteUpdateView.as_view(), name="docente_update"),
    path("<int:pk>/eliminar/", DocenteDeleteView.as_view(), name="docente_delete"),
]