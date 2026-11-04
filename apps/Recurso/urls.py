from django.urls import path
from .views import (RecursoListView, RecursoDetailView, RecursoCreateView, RecursoUpdateView, RecursoDeleteView)

app_name = "recurso"

urlpatterns = [
    path("", RecursoListView.as_view(), name="recurso_list"),
    path("nuevo/", RecursoCreateView.as_view(), name="recurso_create"),
    path("<int:pk>/", RecursoDetailView.as_view(), name="recurso_detail"),
    path("<int:pk>/editar/", RecursoUpdateView.as_view(), name="recurso_update"),
    path("<int:pk>/eliminar/", RecursoDeleteView.as_view(), name="recurso_delete"),
]