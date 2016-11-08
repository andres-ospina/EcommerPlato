from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from apps.comprador.forms import RegistroForm

# Create your views here.


class RegistroComprador(CreateView):
    model = User
    template_name = 'comprador/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('plato:plato_listar')