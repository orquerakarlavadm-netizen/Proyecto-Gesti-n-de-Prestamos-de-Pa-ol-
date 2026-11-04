from django.urls import path
from .views import (ReservaListView, ReservaDetailView, ReservaCreateView, ReservaUpdateView, ReservaDeleteView)

app_name = "reserva"

urlpatterns = [
    path("", ReservaListView.as_view(), name="reserva_list"),
    path("nueva/", ReservaCreateView.as_view(), name="reserva_create"),
    path("<int:pk>/", ReservaDetailView.as_view(), name="reserva_detail"),
    path("<int:pk>/editar/", ReservaUpdateView.as_view(), name="reserva_update"),
    path("<int:pk>/eliminar/", ReservaDeleteView.as_view(), name="reserva_delete"),
]