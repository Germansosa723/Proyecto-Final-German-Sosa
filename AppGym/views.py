from django.shortcuts import render
from AppGym.models import Rutina, Profile, Mensaje
from AppGym.forms import RutinaForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, "AppGym/index.html")

def sobremi(request):
    return render(request, "AppGym/sobre_mi.html")

class RutinaList(ListView): 
    model = Rutina

class RutinaMineList(LoginRequiredMixin,RutinaList):

    def get_queryset(self):
        return Rutina.objects.filter(publicador=self.request.user.id).all()

class RutinaDetail(DetailView):
    model = Rutina

class RutinaDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Rutina
    success_url = reverse_lazy("rutina-list")

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get("pk")
        return Rutina.objects.filter(publicador=user_id,id=post_id).exists()

class RutinaCreate(LoginRequiredMixin,CreateView):
    model = Rutina
    success_url = reverse_lazy("rutina-list")
    fields = '__all__'

class RutinaUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Rutina
    success_url = reverse_lazy("rutina-list")
    fields = '__all__'

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get("pk")
        return Rutina.objects.filter(publicador=user_id,id=post_id).exists()

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


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('rutina-list')

class ProfileCreate(CreateView):
    model = Profile
    success_url = reverse_lazy("rutina-list")
    fields = ['avatar']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfileUpdate(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Profile
    success_url = reverse_lazy("rutina-list")
    fields = ['avatar',]

    def test_func(self):
        return Profile.objects.filter(user=self.request.user).exists()

class MensajeCreate(CreateView):
    model = Mensaje
    success_url = reverse_lazy('mensaje-create')
    fields = '__all__'


class MensajeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mensaje
    context_object_name = "mensaje"
    success_url = reverse_lazy("mensaje-list")

    def test_func(self):
        return Mensaje.objects.filter(destinatario=self.request.user).exists()
    

class MensajeList(LoginRequiredMixin, ListView):
    model = Mensaje
    context_object_name = "mensajes"

    def get_queryset(self):
        import pdb; pdb.set_trace
        return Mensaje.objects.filter(destinatario=self.request.user).all()

