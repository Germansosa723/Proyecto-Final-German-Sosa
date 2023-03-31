from django.shortcuts import render
from AppGym.models import Rutina
from AppGym.forms import RutinaForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

def index(request):
    return render(request, "AppGym/index.html")

class RutinaList(ListView): 
    model = Rutina

class RutinaDetail(DetailView):
    model = Rutina

class RutinaDelete(DeleteView):
    model = Rutina
    success_url = reverse_lazy("rutina-list")

class RutinaCreate(CreateView):
    model = Rutina
    success_url = reverse_lazy("rutina-list")
    fields = '__all__'

class RutinaUpdate(UpdateView):
    model = Rutina
    success_url = reverse_lazy("rutina-list")
    fields = '__all__'

class RutinaSearch(ListView):
    model = Rutina
    
    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        result = (Rutina.objects
        .filter(titulo_rutina=criterio)
        .order_by("creado_el")
        .all())
        return result
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Resultados"
        return context