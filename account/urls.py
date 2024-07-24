from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
path('logout/', LogoutView.as_view(), name='logout'),
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
path('buscar-clases-por-materia/', views.buscar_clases_por_materia, name='buscar_clases_por_materia'),
  path('reset_password/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
path('buscar-clases-por-materia2/', views.buscar_clases_por_materia2, name='buscar_clases_por_materia2'),
path('buscar_clases2/', views.buscar_clases2, name='buscar_clases2'),
]



