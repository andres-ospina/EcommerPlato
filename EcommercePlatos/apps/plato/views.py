from django.shortcuts import render,redirect
from django.views.generic import ListView,CreateView,UpdateView
from apps.plato.models import Plato
from apps.plato.forms import PlatoForm,PlatoFormImagen
from django.core.urlresolvers import reverse_lazy

# Create your views here.


class MostrarPlato(ListView):
    model = Plato
    template_name = 'plato/mostrar_listar.html'
    paginate_by = 9



class RegistrarPlato(CreateView):
    model = Plato
    form_class = PlatoForm
    template_name = 'plato/plato_form.html'
    success_url= reverse_lazy('plato:plato_listar')

def plato_registrar(request):
    if request.method == 'POST':
        form = PlatoFormImagen(request.POST, request.FILES)
        if form.is_valid():
            form.imagen =  request.FILES['imagen']
            form.save()
        return redirect('plato:plato_listar')
    else:
        form = PlatoForm()

    return render(request,'plato/plato_form.html',{'form':form})


class PlatoUpdate(UpdateView):
    model = Plato
    form_class = PlatoForm
    template_name = 'plato/plato_form.html'
    success_url= reverse_lazy('plato:plato_listar')
