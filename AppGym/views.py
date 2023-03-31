from django.shortcuts import render
from AppGym.models import Rutina
from AppGym.forms import RutinaForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, "AppGym/index.html")

class RutinaList(ListView): 
    model = Rutina

class RutinaDetail(DetailView):
    model = Rutina

class RutinaDelete(LoginRequiredMixin,DeleteView):
    model = Rutina
    success_url = reverse_lazy("rutina-list")

class RutinaCreate(LoginRequiredMixin,CreateView):
    model = Rutina
    success_url = reverse_lazy("rutina-list")
    fields = '__all__'

class RutinaUpdate(LoginRequiredMixin,UpdateView):
    model = Rutina
    success_url = reverse_lazy("rutina-list")
    fields = '__all__'

class RutinaSearch(ListView):
    model = Rutina
    context_object_name = "rutinas"

    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        result = Rutina.objects.filter(titulo_rutina__icontains=criterio).all()
        return result
    
class Login(LoginView):
    next_page = reverse_lazy('rutina-list')

class Logout(LogoutView):
     template_name = ("registration/logout.html")


class SignUp(FormView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('rutina-list')