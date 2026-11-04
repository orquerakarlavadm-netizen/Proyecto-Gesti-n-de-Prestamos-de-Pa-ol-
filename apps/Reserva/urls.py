from django.urls import path
from .views import ReservaCreateView, ReservaDeleteView, ReservaDetailView, ReservaListView, ReservaUpdateView

app_name = 'reservas'

urlpatterns = [
    path('reservas/', ReservaListView.as_view(), name='reserva_list'),
    path('reservas/<int:pk>/', ReservaDetailView.as_view(), name='reserva_detail'),
    path('reservas/nueva/', ReservaCreateView.as_view(), name='reserva_create'),
    path('reservas/<int:pk>/editar/', ReservaUpdateView.as_view(), name='reserva_update'),
    path('reservas/<int:pk>/eliminar/', ReservaDeleteView.as_view(), name='reserva_delete'),
]