from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Clase

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_docente', 'is_funcionario')

class ClaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Establecer el valor predeterminado para el campo 'carrera'
        self.fields['carrera'].initial = 'Ingeniería en Informática'
    class Meta:
        model = Clase
        fields = ('carrera', 'curso', 'materia', 'unidad', 'contenido', 'numero_clase', 'fecha', 'hora_inicio', 'hora_fin', 'tipo_clase')
        widgets = {
            'carrera': forms.TextInput(attrs={'class': 'form-control'}),
            'curso': forms.Select(attrs={'class': 'form-control'}),
            'materia': forms.Select(attrs={'class': 'form-control'}),
            'unidad': forms.Select(attrs={'class': 'form-control'}),
            'contenido': forms.Select(attrs={'class': 'form-control'}),
            'numero_clase': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora_inicio': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'hora_fin': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'tipo_clase': forms.Select(attrs={'class': 'form-control'}),
        }