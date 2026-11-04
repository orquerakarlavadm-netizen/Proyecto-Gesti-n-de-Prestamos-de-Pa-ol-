from django.urls import path

from .views import DocenteCreateView, DocenteDeleteView, DocenteDetailView, DocenteListView, DocenteUpdateView

app_name = 'docentes'

urlpatterns = [
    path('docentes/', DocenteListView.as_view(), name='docente_list'),
    path('docentes/<int:pk>/', DocenteDetailView.as_view(), name='docente_detail'),
    path('docentes/nuevo/', DocenteCreateView.as_view(), name='docente_create'),
    path('docentes/<int:pk>/editar/', DocenteUpdateView.as_view(), name='docente_update'),
    path('docentes/<int:pk>/eliminar/', DocenteDeleteView.as_view(), name='docente_delete'),
]