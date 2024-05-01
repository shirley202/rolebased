from django.contrib import admin
from .models import User, Curso, Materia, Unidad, Contenido

# Registrar los modelos en el panel de administración
admin.site.register(User)
admin.site.register(Curso)
admin.site.register(Materia)
admin.site.register(Unidad)  # Corrección del nombre del modelo
admin.site.register(Contenido)
