# Python Automation Tools

Colección de herramientas Python para automatización, procesamiento de datos, administración de archivos y utilidades de soporte.

Estas herramientas fueron diseñadas para resolver tareas comunes relacionadas con:

- Procesamiento de archivos grandes.
- Validación y limpieza de datos.
- Inventarios de directorios.
- Gestión de horarios.
- Automatización de tareas repetitivas.

---

# Herramientas incluidas

## Excel Splitter

Divide archivos Excel grandes en múltiples archivos más pequeños.

Características:

- Conserva encabezados.
- Bajo consumo de memoria.
- Compatible con archivos grandes.

Ubicación:

```text
excel-splitter/
```

---

## CSV Repair Tool

Valida y repara archivos CSV.

Incluye:

- Validación estructural.
- Detección de errores.
- Limpieza de registros corruptos.
- Generación de logs.

Ubicación:

```text
csv-repair-tool/
```

---

## Large File Copy

Copia archivos grandes utilizando lectura por bloques.

Características:

- Bajo consumo de memoria.
- Progreso en tiempo real.
- Compatible con archivos de varios GB.

Ubicación:

```text
large-file-copy/
```

---

## Directory Inventory

Genera inventarios CSV de carpetas y archivos.

Información exportada:

- Ruta completa.
- Nombre.
- Extensión.
- Tamaño.
- Fecha de modificación.

Ubicación:

```text
directory-inventory/
```

---

## Time 1440 Helper

Utilidad para trabajar con horarios utilizando representación basada en minutos.

Ideal para:

- Turnos.
- Horarios rotativos.
- Guardias.
- Validaciones horarias.

Ubicación:

```text
time-1440-helper/
```

---

# Requisitos

- Python 3.8+
- Windows, Linux o macOS

---

# Instalación

Clonar repositorio:

```bash
git clone https://github.com/xaver76/python-automation-tools.git
```

Ingresar al directorio:

```bash
cd python-automation-tools
```

Instalar dependencias según cada herramienta.

---

# Estructura

```text
python-automation-tools/
│
├── excel-splitter/
├── csv-repair-tool/
├── large-file-copy/
├── directory-inventory/
└── time-1440-helper/
```

---

# Roadmap

Próximas herramientas:

- CSV Splitter
- Excel to CSV Converter
- File Hash Checker
- Duplicate Finder
- Log Analyzer
- SQL Exporter

---

# Licencia

MIT License
