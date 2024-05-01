from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, ClaseForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Unidad, Contenido

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
            clase_instance = form.save(commit=False)
            unidad_ids = request.POST.getlist('unidades')  # Obtén la lista de IDs de unidades seleccionadas
            contenido_ids = request.POST.getlist('contenidos')  # Obtén la lista de IDs de contenidos seleccionados
            unidades = Unidad.objects.filter(id__in=unidad_ids)  # Filtra las unidades por los IDs seleccionados
            contenidos = Contenido.objects.filter(id__in=contenido_ids)  # Filtra los contenidos por los IDs seleccionados
            clase_instance.save()  # Guarda la instancia de clase primero para obtener el ID
            clase_instance.unidades.set(unidades)  # Asigna las unidades utilizando el método set()
            clase_instance.contenidos.set(contenidos)  # Asigna los contenidos utilizando el método set()
            messages.success(request, '¡Clase registrada exitosamente!')
            return redirect('docente')
        else:
            errors = form.errors
            return render(request, 'registrar_clase.html', {'form': form, 'errors': errors})
    else:
        form = ClaseForm()
    return render(request, 'registrar_clase.html', {'form': form})



def funcionario(request):
    return render(request,'funcionario.html')