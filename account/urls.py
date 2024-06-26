from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('docente/', views.docente, name='docente'),
    path('funcionario/', views.funcionario, name='funcionario'),
path('confirmation_clase/', views.confirmation_clase, name='confirmation_clase'),
    path('informes/', views.informes_clases, name='informes_clases'),
path('obtener_unidades_y_contenidos/', views.obtener_unidades_y_contenidos, name='obtener_unidades_y_contenidos'),
path('buscar_clases/', views.buscar_clases, name='buscar_clases'),
path('upload/', views.upload_document, name='upload_document'),
    path('ver-asistencia-docente/', views.ver_asistencia_docente, name='ver_asistencia_docente'),



]