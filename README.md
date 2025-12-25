# BiciBlog - Registro de Kilómetros y Pedidos

Este es un proyecto web desarrollado con **Python y Django** que permite registrar los kilómetros recorridos, dinero recaudado y pedidos entregados, así como ver estadísticas y administrar un perfil de usuario.

---
Usuario de prueba

Para poder ver las estadísticas y probar la aplicación, utiliza el siguiente usuario de prueba:

Usuario: fabyss

Contraseña: coder123
## Características

- Registro y login de usuarios.
- Crear, editar y eliminar posts con:
  - Imagen
  - Kilómetros recorridos
  - Dinero recaudado
  - Pedidos entregados
  - Fecha (seleccionable con calendario)
- Visualización de estadísticas acumuladas por usuario.
- Perfil de usuario con avatar y opción de cambiar contraseña.
- Navbar con enlaces a Inicio, Buscar por fecha, Crear Post, Estadísticas, Perfil y Acerca de mí.

---

## Requisitos

- Python 3.12+
- Django 5.1+
- SQLite (incluido por defecto)

---

## Instalación y ejecución local

1. Clona el repositorio:

```bash
git clone https://github.com/ferreirafabian/python_final_Ferreira.git
cd python_final_Ferreira
Crea un entorno virtual (opcional pero recomendado):

python -m venv venv


Activa el entorno virtual:

En Windows:

venv\Scripts\activate


En macOS/Linux:

source venv/bin/activate


Instala las dependencias:

pip install -r requirements.txt


Si no tienes requirements.txt, instala Django manualmente:

pip install django


Aplica las migraciones:

python manage.py makemigrations
python manage.py migrate


Crea un usuario de prueba (ya existe uno, ver más abajo) o usa el superusuario si quieres:

python manage.py createsuperuser

Usuario de prueba

Para poder ver las estadísticas y probar la aplicación, utiliza el siguiente usuario de prueba:

Usuario: fabyss

Contraseña: coder123

Correr el servidor
python manage.py runserver


Abre tu navegador en:

http://127.0.0.1:8000/


Inicia sesión con el usuario de prueba fabyss para ver los posts y estadísticas.
