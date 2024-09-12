from django.shortcuts import render
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy

# Create your views here.

class LoginView(BaseLoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("login")
