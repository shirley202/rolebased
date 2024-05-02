from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Clase, Contenido, Unidad

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
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2', 'is_admin', 'is_docente', 'is_funcionario')

class ClaseForm(forms.ModelForm):
    unidades = forms.ModelMultipleChoiceField(queryset=Unidad.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}), required=True)
    contenidos = forms.ModelMultipleChoiceField(queryset=Contenido.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}), required=True)

    def __init__(self, *args, **kwargs):
        super(ClaseForm, self).__init__(*args, **kwargs)
        # Set initial value for carrera field
        self.fields['carrera'].initial = 'Ingeniería en Informática'

    class Meta:
        model = Clase
        fields = ('carrera', 'curso','semestre', 'materia', 'numero_clase', 'fecha', 'hora_inicio', 'hora_fin', 'tipo_clase','numero_alumno','metodologia','unidades','contenidos')
        widgets = {
            'curso': forms.Select(attrs={'class': 'form-control'}),
            'semestre': forms.Select(attrs={'class': 'form-control'}),
            'materia': forms.Select(attrs={'class': 'form-control'}),
            'numero_clase': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora_inicio': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'hora_fin': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'tipo_clase': forms.Select(attrs={'class': 'form-control'}),
            'numero_alumno': forms.NumberInput(attrs={'class': 'form-control'}),
            'metodologia': forms.TextInput(attrs={'class': 'form-control'}),
        }