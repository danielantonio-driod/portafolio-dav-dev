# 🚀 dlabs Django Maker LITE

**Generador automático de proyectos Django 
> **PyStarter por:** [dav-dev.dev](https://dav-dev.dev) / Daniel Arrieta Vega  
> **Fecha:** Octubre 2025  
> **Versión:** LITE (Community Edition)  
> **Licencia:** MIT

---

## 📖 Descripción

**dlabs Django Maker LITE** es una herramienta gratuita para la comunidad de desarrolladores que automatiza la creación de proyectos Django completos con un solo clic. Incluye:

- ✅ Generación automática de proyectos Django 5.2.7
- ✅ Portal de autenticación pre-configurado
- ✅ Gestión de perfiles de usuario
- ✅ Templates básicos incluidos
- ✅ Soporte para SQLite, PostgreSQL y MySQL
- ✅ Interfaz gráfica retro (estilo Nokia 3310)
- ✅ Ejecutable único de 10 MB

---

## 🎯 Características Principales

### 🏗️ Creación de Proyectos
- **Generación automática** de estructura Django completa
- **Entorno virtual** creado automáticamente
- **App 'core'** pre-configurada con:
  - Sistema de autenticación (login/logout)
  - Gestión de perfiles de usuario
  - Páginas de error personalizadas (404, 500)
  - Templates base con Bootstrap 5

### 📦 Gestión de Apps
- **Templates de aplicaciones** incluidos:
  - `basic_app`: CRUD básico con modelo Item
  - `contact_form`: Formulario de contacto con validación
- **Integración automática**:
  - Configuración en `INSTALLED_APPS`
  - URLs configuradas automáticamente
  - Migraciones ejecutadas
  - Navegación actualizada

### 🗄️ Soporte de Bases de Datos
- **SQLite** (por defecto, sin configuración)
- **PostgreSQL** (instalación automática de driver)
- **MySQL** (instalación automática de driver)
- **Fallback inteligente** a SQLite si falla instalación

### 🚀 Preparación para Producción
- **Verificación de seguridad**:
  - Detección de DEBUG=True
  - Validación de SECRET_KEY
  - Verificación de ALLOWED_HOSTS
- **Archivos generados**:
  - `requirements.txt`
  - `.env.example`
  - `.gitignore`
  - `PRODUCTION_CHECKLIST.md`
- **Collectstatic** ejecutado automáticamente

### 🎨 Interfaz Retro
- **Tema Nokia 3310** oscuro (#223355)
- **Consola integrada** con logs en tiempo real
- **Barras de progreso** para operaciones largas
- **Diálogos informativos** con emojis
- **Interfaz bilingüe** (ES/EN) con detección automática

---

## 🖥️ Requisitos del Sistema

- **Sistema Operativo:** Windows 10/11, Linux, macOS
- **Python:** 3.13+ (incluido en el ejecutable)
- **Espacio en disco:** ~50 MB para el programa + proyectos
- **RAM:** 256 MB mínimo

---

## 📥 Instalación


1. Descarga `dlabs-django-maker-lite.exe` (10 MB)
2. Ejecuta el archivo
3. ¡Listo! No requiere instalación

---

## 🚀 Guía de Uso Rápido

### 1️⃣ Crear Proyecto

1. Abre **dlabs Django Maker LITE**
2. Completa los campos:
   - **Nombre del proyecto:** `miproyecto`
   - **Entorno virtual:** `venv`
   - **Usuario admin:** `admin`
   - **Email:** `admin@example.com`
   - **Password:** Tu contraseña
   - **Base de datos:** SQLite / PostgreSQL / MySQL
3. Click en **"Crear Proyecto"**
4. Selecciona carpeta de destino
5. Espera a que termine (~2-3 minutos)

### 2️⃣ Explorar el Proyecto

```bash
cd ruta/a/tu/proyecto
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Iniciar servidor
python manage.py runserver

# Visitar
http://127.0.0.1:8000/
```

### 3️⃣ Crear Nueva App

1. Click en **"Crear App"**
2. Selecciona template:
   - **Basic App:** CRUD simple
   - **Contact Form:** Formulario de contacto
3. Ingresa nombre de la app: `productos`
4. ¡Listo! La app se integra automáticamente

### 4️⃣ Preparar para Producción

1. Click en **"Preparar para Producción"**
2. Revisa advertencias de seguridad
3. Edita `.env.example` → `.env` con tus credenciales
4. Sigue el checklist en `PRODUCTION_CHECKLIST.md`

---

## 📁 Estructura del Proyecto Generado

```
miproyecto/
├── manage.py
├── venv/                    # Entorno virtual
├── miproyecto/             # Configuración principal
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                   # App principal pre-configurada
│   ├── models.py          # UserProfile extendido
│   ├── views.py           # Login, logout, profile
│   ├── forms.py           # ProfileForm
│   ├── urls.py
│   └── admin.py
├── templates/             # Templates globales
│   ├── base.html
│   ├── home.html
│   ├── registration/
│   │   └── login.html
│   ├── 404.html
│   └── 500.html
├── static/
│   └── style.css
└── db.sqlite3
```

---

## 🔧 Funciones Avanzadas

### Validación de Templates
- Verificación de sintaxis automática
- Validación de dependencias
- Compatibilidad de versiones Django

### Gestión de Terminales
- **Terminal del servidor:** Se cierra automáticamente al crear nueva app
- **Terminales adicionales:** Para comandos manuales
- **Limpieza inteligente:** No acumula procesos

### Análisis de Proyectos
- Detección de apps existentes
- Verificación de archivos importantes
- Análisis de configuración

---

## 🎓 Templates Incluidos

### 1. Basic App
Genera una app CRUD completa:
- Modelo `Item` con nombre y descripción
- Vistas para listar y crear items
- Formulario con validación
- Templates con Bootstrap
- Admin configurado

### 2. Contact Form
Formulario de contacto profesional:
- Modelo `ContactMessage`
- Validación de email
- Almacenamiento de mensajes
- Panel de administración
- Template responsivo

---

## 🐛 Solución de Problemas

### Error: "Puerto 8000 en uso"
```bash
# El programa lo soluciona automáticamente
# O manualmente:
netstat -ano | findstr :8000
taskkill /F /PID <PID>
```

### Error: "No se encontró entorno virtual"
- Verifica que el nombre del venv coincida
- Usa "Buscar venv manualmente" en el programa

### Error: Driver PostgreSQL/MySQL no instalado
- El programa ofrece automáticamente usar SQLite
- O instala manualmente:
```bash
pip install psycopg2-binary  # PostgreSQL
pip install mysqlclient       # MySQL
```

---

## 📝 Changelog

### v1.0 - LITE Edition (Octubre 2025)
- ✅ Generación automática de proyectos Django 5.2.7
- ✅ Portal de autenticación completo
- ✅ 2 templates básicos incluidos
- ✅ Soporte para 3 bases de datos
- ✅ Instalación automática de drivers
- ✅ Preparación para producción mejorada
- ✅ Gestión dinámica de terminales
- ✅ Interfaz gráfica estilo Nokia 3310
- ✅ 9 bugs críticos corregidos durante desarrollo
- ✅ Interfaz bilingüe (ES/EN) con detección automática

---

## 📄 Licencia

MIT License - Copyright (c) 2025 Daniel Arrieta Vega / dav-dev.dev

Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia de este software y archivos de documentación asociados (el "Software"), para utilizar el Software sin restricciones, incluyendo sin limitación los derechos de usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar y/o vender copias del Software.

---

## 👨‍💻 Autor

**Daniel Arrieta Vega**
- 🌐 Website: [dav-dev.dev](https://dav-dev.dev) (en construcción)
- 📧 Email: nice@dav-dev.dev
- 🐙 GitHub: [github.com/dav-dev](https://github.com/danielantonio-droid)

---

## 🙏 Agradecimientos

- A todos los que usen esta herramienta

---

## 💬 Soporte

- **Issues:** GitHub Issues
- **Discusiones:** GitHub Discussions
- **Email:** contact@dav-dev.dev

---

## 🌍 Idiomas / Languages

- **Español:** README.md (este archivo)
- **English:** [README_EN.md](README_EN.md)

---

<div align="center">

**Hecho con ❤️ por la comunidad de desarrolladores**

**PyStarter** por [dav-dev.dev](https://dav-dev.dev) / Daniel Arrieta Vega © 10-2025

⭐ Si te gusta este proyecto, dale una estrella en GitHub ⭐

</div>
