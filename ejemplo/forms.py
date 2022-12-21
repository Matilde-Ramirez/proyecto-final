from django import forms
from ejemplo.models import Obreros, Obras, Familiar

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)
    widget=forms.TextInput(attrs={'placeholder':'Busque algo'})

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']

class ObrerosForm(forms.ModelForm):
  class Meta:
    model = Obreros
    fields = ['nombre', 'categoria', 'edad']

class ObrasForm(forms.ModelForm):
  class Meta:
    model = Obras
    fields = ['nombre', 'direccion', 'niveles']