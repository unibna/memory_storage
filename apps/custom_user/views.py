from django.db import models
from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.views.generic import CreateView

from .forms import CustomCreationForm



class CustomRegisterView(CreateView):
    model = User
    template_name = "custom_user/register.html"
    form_class = CustomCreationForm
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    template_name = 'custom_user/login.html'
    success_url = reverse_lazy('home')