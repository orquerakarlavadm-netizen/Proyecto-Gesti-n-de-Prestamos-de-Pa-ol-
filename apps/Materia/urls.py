from django.urls import path
from .views import MateriaCreateView, MateriaDeleteView, MateriaDetailView, MateriaListView, MateriaUpdateView

app_name = 'materias'

urlpatterns = [
    path('materias/', MateriaListView.as_view(), name='materia_list'),
    path('materias/<int:pk>/', MateriaDetailView.as_view(), name='materia_detail'),
    path('materias/nueva/', MateriaCreateView.as_view(), name='materia_create'),
    path('materias/<int:pk>/editar/', MateriaUpdateView.as_view(), name='materia_update'),
    path('materias/<int:pk>/eliminar/', MateriaDeleteView.as_view(), name='materia_delete'),
]