from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Materia

class MateriaDetailView(DetailView):
    model = Materia
    template_name = "materia/detalle.html"
    context_object_name = "materia"

class MateriaListView(ListView):
    model = Materia
    template_name = 'materia/list.html'
    context_object_name = 'materias'

class MateriaCreateView(CreateView):
    model = Materia
    fields = '__all__'
    template_name = 'materia/create.html'
    success_url = reverse_lazy('materias:materia_list')

class MateriaUpdateView(UpdateView):
    model = Materia
    fields = '__all__'
    template_name = 'materia/update.html'
    success_url = reverse_lazy('materias:materia_list')

class MateriaDeleteView(DeleteView):
    model = Materia
    template_name = 'materia/delete.html'
    success_url = reverse_lazy('materias:materia_list')