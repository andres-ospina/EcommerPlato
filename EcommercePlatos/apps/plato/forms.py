from django import forms
from apps.plato.models import Plato


class PlatoForm(forms.ModelForm):
    class Meta:
        model = Plato

        fields = [

            'titulo',
            'descripcion',
            'sector_zona',
            'ingrediente',
            'cal_gras_trans',
            'costo',
        ]
        labels = {

            'titulo' : 'Titulo Plato',
            'descripcion' : 'Descripcion',
            'sector_zona' : 'Sector o Zona',
            'ingrediente' : 'Ingredientes',
            'cal_gras_trans':'Calorias o Grasas Trans',
            'costo' : 'Costo  Plato',
        }
        widgets = {

            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control'}),
            'sector_zona': forms.TextInput(attrs={'class': 'form-control'}),
            'ingrediente': forms.Textarea(attrs={'class': 'form-control'}),
            'cal_gras_trans': forms.Textarea(attrs={'class': 'form-control'}),
            'costo': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PlatoFormImagen(forms.ModelForm):
    class Meta:
        model = Plato

        fields = [
            'imagen',

        ]
        labels = {
            'imagen' : 'Foto Plato',

        }
        widgets = {
            'imagen' : forms.ImageField(),

        }
