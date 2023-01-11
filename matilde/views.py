from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from matilde.models import Post
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.admin import User
from matilde.forms import UsuarioForm
from matilde.models import Avatar, Post, Mensaje

 
def index(request):
   posts = Post.objects.order_by('-publicado_el').all()
   return render(request, "matilde/index.html", {"posts": posts})
 
class PostDetalle(DetailView):
   model = Post
 
class PostListar(ListView):
   model = Post 
 
class PostCrear(LoginRequiredMixin,CreateView):
   model = Post
   success_url = reverse_lazy("matilde-listar")
   fields = '__all__'
 
class PostBorrar(LoginRequiredMixin, DeleteView):
   model = Post
   success_url = reverse_lazy("matilde-listar")
 
class PostActualizar(LoginRequiredMixin, UpdateView):
   model = Post
   success_url = reverse_lazy("matilde-listar")
   fields = "__all__"
 
class UserSignUp(CreateView):
   form_class = UsuarioForm
   template_name = 'registration/signup.html'
   success_url = reverse_lazy('matilde-listar')
 
 
class UserLogin(LoginView):
   next_page = reverse_lazy('matilde-listar')
 
class UserLogout(LogoutView):
   next_page = reverse_lazy('matilde-listar')
 
class AvatarActualizar(UpdateView):
   model = Avatar
   fields = ['imagen']
   success_url = reverse_lazy('matilde-listar')
 
 
class UserActualizar(UpdateView):
   model = User
   fields = ['first_name', 'last_name', 'email']
   success_url = reverse_lazy('matilde-listar')
 
 
class MensajeDetalle(DetailView):
   model = Mensaje
 
class MensajeListar(ListView):
   model = Mensaje 
 
class MensajeCrear(CreateView):
   model = Mensaje
   success_url = reverse_lazy("matilde-mensajes-crear")
   fields = ['nombre', 'email', 'texto']
 
class MensajeBorrar(LoginRequiredMixin, DeleteView):
   model = Mensaje
   success_url = reverse_lazy("matilde-mensajes-listar")
