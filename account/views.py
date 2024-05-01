from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, ClaseForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_docente:
                login(request, user)
                return redirect('docente')
            elif user is not None and user.is_funcionario:
                login(request, user)
                return redirect('funcionario')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'admin.html')


def docente(request):
    if request.method == 'POST':
        form = ClaseForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar los datos del formulario en la base de datos
            messages.success(request, '¡Clase registrada exitosamente!')  # Agregar mensaje de éxito
            return redirect('docente')  # Redirigir a la misma página después de guardar
    else:
        form = ClaseForm()  # Crear una instancia del formulario ClaseForm

    return render(request, 'registrar_clase.html', {'form': form})

def funcionario(request):
    return render(request,'funcionario.html')