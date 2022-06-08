from django import forms
from .models import Carrera, Alumno

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ['nombre', 'semestres', 'mensualidad']
        labels = {
            'nombre': 'Nombre',
            'semestres': 'Semestres',
            'mensualidad': 'Mensualidad Pesos Chilenos',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'semestres': forms.TextInput(attrs={'class': 'form-control'}),
            'mensualidad': forms.TextInput(attrs={'class': 'form-control'}),
        }
