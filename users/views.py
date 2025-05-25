from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from  django.contrib.auth import login, logout


# Create your views here.
class UserRegister(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        response = super().form_valid(form) # No utilizo user.save() porque esta linea ya guarda el formulario
        login(self.request, self.object) # Self.object es el usuario
        return response
    
    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form, error="Por favor, corrige los errores.")
        )
    
class UserLogin(LoginView):
    form_class = AuthenticationForm
    template_name = 'user/login.html'

    def get_success_url(self):
        return reverse_lazy('posts')
    
    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form, error="Credenciales inválidas. Intenta nuevamente.")
        )

class UserLogout(LogoutView):
    next_page = reverse_lazy('posts')