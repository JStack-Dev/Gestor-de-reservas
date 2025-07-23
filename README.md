# 🏟️ Gestor de Reservas de Pistas y Salas

Un sistema web desarrollado con **Django** para gestionar reservas de recursos como pistas de pádel, tenis, fútbol o salas multiusos.  
Incluye un **calendario interactivo con FullCalendar**, gestión de usuarios, validación de solapamientos, reservas recurrentes, bloqueos administrativos y un panel de administración completo.

---

## **Características principales**

### **Modelos implementados**
- **Resource** – Representa cada recurso o pista disponible (pádel, fútbol, etc.).
- **Booking** – Registra las reservas de usuarios para un recurso.
- **Availability (Bloqueos)** – Define franjas horarias en las que una pista no está disponible (bloqueos administrativos).
- **User (Autenticación)** – Gestión de usuarios con login/logout.

### **Funcionalidades clave**
- 📅 **Calendario de disponibilidad** con **FullCalendar**.
- ⛔ **Evita solapamiento de reservas** automáticamente.
- 🔁 **Reservas recurrentes** (opción de repetir semanalmente).
- 🔒 **Bloqueos de recursos** gestionados desde el panel de administración.
- 👨💼 **Panel de administración Django Admin** para gestionar usuarios, recursos, reservas y bloqueos.
- 🔔 **Notificaciones al usuario** al crear reservas o cuando se produce un conflicto.

---

## **Tecnologías utilizadas**

- **Backend:** Django 5 (Python 3.12)
- **Frontend:** HTML5, CSS3, JavaScript (con integración de FullCalendar)
- **Base de datos:** SQLite (por defecto, fácil de cambiar a MySQL o PostgreSQL)
- **Autenticación:** Sistema de usuarios de Django
- **UI:** Diseño minimalista con **navbar**, cards y calendario interactivo

---

## Enfoque del Proyecto

Este proyecto está centrado principalmente en el aprendizaje y la práctica de **Django**.  
Mi objetivo ha sido entender la arquitectura del framework, el manejo de vistas, URLs, modelos, templates y la interacción con la base de datos.  

Por este motivo, el **diseño visual** no ha sido la prioridad en esta fase del desarrollo, ya que mi atención ha estado enfocada en construir una aplicación funcional y bien estructurada en cuanto a lógica y backend.



## **Instalación**

### **1. Clonar el repositorio**

git clone https://github.com/tu-usuario/gestor-reservas.git
cd gestor-reservas
2. Crear entorno virtual

python -m venv .venv
source .venv/bin/activate  # En Linux/Mac
.venv\Scripts\activate     # En Windows

3. Instalar dependencias
pip install -r requirements.txt

4. Migrar la base de datos
python manage.py makemigrations
python manage.py migrate

6. Crear un superusuario (para acceder al panel admin)
python manage.py createsuperuser

8. Ejecutar el servidor
python manage.py runserver
Accede en tu navegador a http://127.0.0.1:8000/

Uso de la aplicación
Panel de administración:
Accede a http://127.0.0.1:8000/admin/ para crear recursos (pistas) y gestionar reservas manualmente.

Home Page (Listado de recursos):
Verás todas las pistas (pádel, fútbol, tenis, etc.) con cards interactivas y un botón para ver el calendario de cada una.

Calendario interactivo:

Selecciona un bloque de tiempo disponible para hacer una reserva.

El sistema valida solapamientos y bloqueos.

Se pueden crear reservas recurrentes (pregunta cuántas semanas repetir).
