# Proyecto LexLegal - Sistema de Gestión Jurídica

**LexLegal** es una plataforma integral desarrollada en **Django** diseñada para digitalizar y optimizar los procesos internos de un bufete de abogados o consultoría legal. El sistema gestiona el ciclo de vida completo de la relación cliente-abogado, desde la captación de solicitudes hasta la facturación y seguimiento de casos.

## 🚀 Características Principales

### 👥 Gestión de Usuarios y Roles
- **Portal de Clientes:** Los clientes pueden registrarse, actualizar su información personal y enviar solicitudes de servicios legales.
- **Portal de Empleados:** Los abogados y personal administrativo pueden gestionar solicitudes entrantes, evaluar casos y asignar presupuestos.

### ⚖️ Ciclo de Vida del Caso Legal
- **Flujo de Solicitudes:** Sistema de aprobación de solicitudes ("Solicitud" -> "Solicitud Aceptada" -> "Contrato").
- **Gestión de Casos:** Un caso centraliza toda la información pertinente: el cliente involucrado, el abogado asignado y el contrato vinculante.
- **Seguimiento de Diligencias:** Bitácora integrada para registrar el avance y los hitos (diligencias) de cada caso.

### 📁 Gestión Documental
- **Repositorio Seguro:** Subida y almacenamiento seguro de documentos legales vinculados directamente a su caso correspondiente, facilitando la auditoría y revisión de expedientes.

### 💰 Facturación y Contratos
- **Contratos:** Creación de contratos con montos y fechas específicas al momento de formalizar un caso.
- **Control de Pagos:** Módulo para la emisión de boletas y el registro de pagos asociados a los contratos, manteniendo un control financiero por caso.

## 🛠️ Stack Tecnológico
- **Backend:** Python 3.x, Django
- **Base de Datos:** SQLite (Configurada para entorno de desarrollo, migrable a PostgreSQL/MySQL)
- **Frontend:** Django Templates con HTML/CSS nativo
- **Gestión de Archivos:** Django File handling para documentos y evidencias (`FileField`)

## 📋 Requisitos
- Python 3.10+
- Pip (gestor de paquetes de Python)

## 🔧 Instalación y Despliegue

1. **Clonar el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   cd ProyectoLexLegal
   ```

2. **Crear y activar un entorno virtual:**
   ```bash
   python -m venv venv
   # En Windows:
   .\venv\Scripts\activate
   # En Linux/Mac:
   source venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install django
   ```

4. **Realizar migraciones de la base de datos:**
   ```bash
   python manage.py makemigrations Webapp
   python manage.py migrate
   ```

5. **Iniciar el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

## 📂 Estructura de la Base de Datos (Modelos Clave)
- `Cliente` / `Empleado` / `TipoEmpleado`
- `Solicitud` / `Solicitud_Aceptada`
- `Contrato` / `Caso` / `Diligencia`
- `Documento` / `Boleta` / `Pago`

---
*Desarrollado como proyecto semestral de Ingeniería de Software, demostrando capacidades en modelado de datos relacionales complejos, flujos de estado de negocio y desarrollo de aplicaciones web MVC/MVT con Django.*
