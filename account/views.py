from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, ClaseForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Unidad, Contenido, Clase
from django.http import JsonResponse

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
            clase_instance.usuario = request.user
            unidad_ids = request.POST.getlist('unidades')  # Obtén la lista de IDs de unidades seleccionadas
            contenido_ids = request.POST.getlist('contenidos')  # Obtén la lista de IDs de contenidos seleccionados
            unidades = Unidad.objects.filter(id__in=unidad_ids)  # Filtra las unidades por los IDs seleccionados
            contenidos = Contenido.objects.filter(id__in=contenido_ids)  # Filtra los contenidos por los IDs seleccionados
            clase_instance.save()  # Guarda la instancia de clase primero para obtener el ID
            clase_instance.unidades.set(unidades)  # Asigna las unidades utilizando el método set()
            clase_instance.contenidos.set(contenidos)  # Asigna los contenidos utilizando el método set()
            messages.success(request, '¡Clase registrada exitosamente!')
            return redirect('confirmation_clase')
        else:
            errors = form.errors
            return render(request, 'registrar_clase.html', {'form': form, 'errors': errors})
    else:
        form = ClaseForm()
    return render(request, 'registrar_clase.html', {'form': form})






def view_clases(request):
    clases = Clase.objects.all()
    return render(request, 'clases.html', {'clases': clases})
def funcionario(request):
    clases = Clase.objects.all()
    return render(request, 'clases.html', {'clases': clases})
def confirmation_clase(request):
    # Recuperar la última clase registrada por el usuario actual
    latest_clase = Clase.objects.filter(usuario=request.user).last()

    # Verificar si se encontró una clase
    if latest_clase:
        # Pasar la instancia de la clase como parte del contexto
        return render(request, 'confirmacion_clase.html', {'clase': latest_clase})
    else:
        # Si no se encuentra ninguna clase, manejar el caso en consecuencia
        return render(request, 'confirmacion_clase.html', {'error': 'No se encontraron clases registradas'})

def informes_clases(request):
    # Filtrar las clases por el docente que ha iniciado sesión
    clases_docente = Clase.objects.filter(usuario=request.user)

    # Renderizar la plantilla con las clases del docente
    return render(request, 'informes_clases.html', {'clases': clases_docente})

def obtener_unidades_y_contenidos(request):
    materia_id = request.GET.get('materia_id')
    unidades = Unidad.objects.filter(materia_id=materia_id)
    contenidos = Contenido.objects.filter(unidad__materia_id=materia_id)

    unidades_data = [{'id': unidad.id, 'nombre': unidad.nombre} for unidad in unidades]
    contenidos_data = [{'id': contenido.id, 'nombre': contenido.nombre} for contenido in contenidos]

    data = {'unidades': unidades_data, 'contenidos': contenidos_data}
    return JsonResponse(data)