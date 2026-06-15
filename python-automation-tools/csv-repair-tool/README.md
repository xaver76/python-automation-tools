# CSV Repair Tool

Herramienta para validar y reparar archivos CSV grandes de forma eficiente, utilizando procesamiento por streaming para minimizar el consumo de memoria.

Ideal para:

- Archivos CSV de cientos de miles o millones de registros.
- Procesos ETL.
- Migraciones de datos.
- Importaciones a MySQL, MariaDB, PostgreSQL o SQL Server.
- Detección de registros corruptos.

---

# Características

✅ Procesamiento por streaming.

✅ Bajo consumo de memoria.

✅ Compatible con archivos de varios GB.

✅ Validación de estructura.

✅ Detección de filas inconsistentes.

✅ Registro de errores en archivo de log.

✅ Continúa procesando aunque encuentre errores.

✅ Sin dependencias externas.

---

# Estructura del proyecto

```text
csv-repair-tool/
│
├── repair_csv.py
├── validate_csv.py
├── requirements.txt
├── README.md
└── logs/
```

---

# Requisitos

- Python 3.8 o superior

---

# Instalación

Clonar el repositorio:

```bash
git clone https://github.com/usuario/csv-repair-tool.git
cd csv-repair-tool
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

# Herramientas incluidas

## 1. validate_csv.py

Permite validar la estructura del archivo CSV.

Verifica:

- Cantidad de columnas.
- Filas inconsistentes.
- Errores de lectura.
- Registros potencialmente corruptos.

### Uso

```bash
python validate_csv.py archivo.csv
```

### Separador personalizado

```bash
python validate_csv.py archivo.csv --delimiter ","
```

### Log personalizado

```bash
python validate_csv.py archivo.csv --log validacion.log
```

### Ejemplo de salida

```text
========== RESUMEN ==========
Archivo          : clientes.csv
Filas procesadas : 250000
Filas válidas    : 249998
Filas con error  : 2
Log generado     : validacion.log
============================
```

---

## 2. repair_csv.py

Genera una nueva copia del archivo eliminando filas corruptas.

### Uso

```bash
python repair_csv.py origen.csv limpio.csv
```

### Separador personalizado

```bash
python repair_csv.py origen.csv limpio.csv --delimiter ","
```

### Log personalizado

```bash
python repair_csv.py origen.csv limpio.csv --log errores.log
```

### Ejemplo de salida

```text
Procesadas: 10000
Procesadas: 20000
Procesadas: 30000

========== RESUMEN ==========
Filas procesadas : 30000
Filas válidas    : 29998
Filas con error  : 2
============================
```

---

# Casos de uso

### Limpieza previa a importaciones

```bash
python repair_csv.py ventas.csv ventas_limpio.csv
```

### Auditoría de archivos recibidos

```bash
python validate_csv.py clientes.csv
```

### Validación de exportaciones de sistemas externos

```bash
python validate_csv.py exportacion.csv
```

---

# Limitaciones actuales

La versión actual detecta y registra errores, pero no intenta reconstruir registros dañados.

Ejemplos:

```csv
"Juan";"Perez;"Buenos Aires"
```

```csv
"Cliente
con salto de línea";"Activo"
```

Estos casos serán abordados en futuras versiones.

---

# Roadmap

## Versión 2

- Detección automática de delimitador.
- Barra de progreso.
- Estadísticas avanzadas.
- Reconstrucción de registros partidos.
- Corrección automática de comillas desbalanceadas.
- Soporte para archivos comprimidos.

## Versión 3

- Interfaz gráfica.
- Exportación de reportes.
- Modo batch para múltiples archivos.

---

# Dependencias

Actualmente no requiere librerías externas.

```txt
Standard Library Only
```

---

# Licencia

MIT License

---

# Autor

Proyecto desarrollado para tareas de automatización, validación y procesamiento de grandes volúmenes de datos.
