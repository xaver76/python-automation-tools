# Directory Inventory

Herramienta para generar inventarios completos de archivos dentro de una carpeta.

Recorre directorios de forma recursiva y exporta la información a un archivo CSV.

---

# Características

- Exploración recursiva.
- Exportación CSV.
- Compatible con grandes volúmenes de archivos.
- Bajo consumo de memoria.
- Sin dependencias externas.

---

# Información exportada

Cada archivo incluye:

- Ruta completa
- Carpeta
- Nombre de archivo
- Extensión
- Tamaño en bytes
- Tamaño legible
- Fecha de modificación

---

# Uso

```bash
python directory_inventory.py "D:\Datos" inventario.csv
```

---

# Ejemplo de salida

```csv
ruta_completa;carpeta;archivo;extension;tamano_bytes;tamano_legible;fecha_modificacion
D:\Datos\archivo1.pdf;D:\Datos;archivo1.pdf;.pdf;1048576;1.00 MB;2026-06-15 10:15:20
D:\Datos\archivo2.xlsx;D:\Datos;archivo2.xlsx;.xlsx;524288;512.00 KB;2026-06-15 11:20:55
```

---

# Resumen final

```text
========== RESUMEN ==========
Carpeta analizada : D:\Datos
Archivos          : 12,540
Tamaño total      : 25.43 GB
Archivo generado  : inventario.csv
============================
```

---

# Casos de uso

- Inventarios de servidores.
- Auditorías.
- Migraciones.
- Análisis de almacenamiento.
- Control documental.
- Backups.

---

# Dependencias

```txt
Standard Library Only
```

---

# Licencia

MIT License
