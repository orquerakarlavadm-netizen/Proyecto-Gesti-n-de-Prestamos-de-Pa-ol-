from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Docente

class DocenteDetailView(DetailView):
    model = Docente
    template_name = "docente/detalle.html"
    context_object_name = "docente"

class DocenteListView(ListView):
    model = Docente
    template_name = 'docente/list.html'
    context_object_name = 'docentes'

class DocenteCreateView(CreateView):
    model = Docente
    fields = '__all__'
    template_name = 'docente/create.html'
    success_url = reverse_lazy('docentes:docente_list')

class DocenteUpdateView(UpdateView):
    model = Docente
    fields = '__all__'
    template_name = 'docente/update.html'
    success_url = reverse_lazy('docentes:docente_list')

class DocenteDeleteView(DeleteView):
    model = Docente
    template_name = 'docente/delete.html'
    success_url = reverse_lazy('docentes:docente_list')