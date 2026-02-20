🎓 Role Based Login System
<p align="center">










</p>

Sistema web desarrollado en Django que implementa autenticación basada en roles y gestión académica de clases, materias y contenidos, incluyendo carga automatizada de programas desde archivos .docx.

📌 Descripción

Este sistema permite gestionar clases académicas diferenciando permisos según el tipo de usuario:

👨‍💼 Administrador

👨‍🏫 Docente

🏢 Funcionario

Incluye registro de clases, asociación de materias y contenidos, búsqueda avanzada y procesamiento automático de programas académicos.

🛠 Tech Stack
🔹 Backend

Python 3

Django 3.1

Custom User Model

🔹 Base de Datos

SQLite (por defecto)

Compatible con MySQL

🔹 Autenticación y Seguridad

django-allauth

bcrypt

OAuth support

🔹 Procesamiento de Documentos

python-docx

pdfplumber

tabula

camelot

🔹 Otros

Stripe (configurable)

Pillow

django-widget-tweaks

🏗 Arquitectura del Proyecto
Role_based_login_system/
│
├── manage.py
├── requirements
├── Role_based_login_system/   # Configuración principal
├── account/                   # App principal
├── templates/
├── static/
└── db.sqlite3
👥 Sistema de Roles

El sistema utiliza un modelo de usuario personalizado con los siguientes flags:

is_admin

is_docente

is_funcionario

Cada rol es redirigido automáticamente a su panel correspondiente tras autenticarse.

🚀 Funcionalidades Principales
🔐 Autenticación

Registro de usuarios

Login con redirección basada en rol

Control de acceso por permisos

👨‍🏫 Gestión de Clases

Registro de clases académicas

Asociación dinámica de unidades y contenidos

Selección de tipo de clase (Teórica / Práctica / Laboratorio)

Registro de cantidad de alumnos

🔎 Sistema de Búsqueda

Filtro por docente

Filtro por materia

Filtro por rango horario

Consulta de asistencia docente

📄 Carga Automática de Programa Académico

Permite subir un archivo .docx que contenga:

Semestre

Materia

Unidades

Contenidos

El sistema procesa el documento mediante expresiones regulares y genera automáticamente los registros correspondientes en la base de datos.

⚙️ Instalación
1️⃣ Clonar el repositorio
git clone https://github.com/TU-USUARIO/TU-REPO.git
cd Role_based_login_system
2️⃣ Crear entorno virtual
python -m venv venv

Activar entorno:

Linux / Mac:

source venv/bin/activate

Windows:

venv\Scripts\activate
3️⃣ Instalar dependencias
pip install -r requirements
4️⃣ Aplicar migraciones
python manage.py migrate
5️⃣ Crear superusuario
python manage.py createsuperuser
6️⃣ Ejecutar servidor
python manage.py runserver
📌 Endpoints Principales
Ruta	Funcionalidad
/register/	Registro de usuario
/login/	Inicio de sesión
/docente/	Panel docente
/funcionario/	Panel funcionario
/upload_document/	Subida de programa académico
/clases/	Visualización de clases
🔐 Seguridad

Modelo de usuario personalizado

Hashing con bcrypt

Integración con OAuth

Preparado para integración de pagos con Stripe


🎯 Objetivo del Proyecto

Demostrar:

Implementación de autenticación basada en roles

Modelado relacional avanzado en Django

Procesamiento automático de documentos

Gestión académica estructurada

Organización modular de aplicaciones Django

👤 Autor

Shirley Lesme

GitHub: https://github.com/shirley202