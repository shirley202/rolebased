🎓 Role Based Login System
<p align="left"> <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/Django-3.1-green?logo=django&logoColor=white"/> <img src="https://img.shields.io/badge/DB-SQLite-lightgrey?logo=sqlite&logoColor=white"/> <img src="https://img.shields.io/badge/Compatible-MySQL-orange?logo=mysql&logoColor=white"/> </p>

Sistema web desarrollado en Django 3.1 que implementa autenticación basada en roles y gestión académica de clases, materias y contenidos, con carga automatizada de programas desde documentos Word.

🚀 Features

🔐 Autenticación con roles (Admin / Docente / Funcionario)

👨‍🏫 Registro de clases

🔎 Filtros por docente y materia

📄 Carga automática de programa académico (.docx)

🛠 Tech Stack

Backend: Python, Django 3.1
DB: SQLite (default), MySQL compatible
Auth: django-allauth, bcrypt
Docs: python-docx, pdfplumber, tabula, camelot

🏗
👥 Roles

Custom User Model:

is_admin

is_docente

is_funcionario

Redirección automática según rol tras login.

⚙️ Installation
git clone https://github.com/shirley202/rolebased.git
cd Role_based_login_system
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements
python manage.py migrate
python manage.py runserver


🎯 Objetivo

Proyecto enfocado en demostrar:

Role-based authentication

Modelado relacional en Django

Automatización de carga académica

👤 Author

Shirley Lesme
https://github.com/shirley202