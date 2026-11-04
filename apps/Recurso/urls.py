from django.urls import path
from .views import RecursoCreateView, RecursoDeleteView, RecursoDetailView, RecursoListView, RecursoUpdateView

app_name = 'recursos'

urlpatterns = [
    path('recursos/', RecursoListView.as_view(), name='recurso_list'),
    path('recursos/<int:pk>/', RecursoDetailView.as_view(), name='recurso_detail'),
    path('recursos/nueva/', RecursoCreateView.as_view(), name='recurso_create'),
    path('recursos/<int:pk>/editar/', RecursoUpdateView.as_view(), name='recurso_update'),
    path('recursos/<int:pk>/eliminar/', RecursoDeleteView.as_view(), name='recurso_delete'),
]