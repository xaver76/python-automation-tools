# Excel Splitter

Herramienta en Python para dividir archivos Excel grandes (.xlsx) en múltiples archivos más pequeños.

Ideal para:

- Procesar archivos que exceden límites de memoria.
- Compartir grandes volúmenes de datos.
- Facilitar importaciones masivas.
- Trabajar con archivos que contienen cientos de miles de registros.

## Características

- Conserva la fila de encabezados en cada archivo generado.
- Permite definir la cantidad de filas por archivo.
- Soporta hojas específicas.
- Bajo consumo de memoria mediante lectura en modo `read_only`.
- Compatible con archivos `.xlsx`.

## Requisitos

- Python 3.8 o superior

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/usuario/excel-splitter.git
cd excel-splitter
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Uso básico

```bash
python split_excel.py archivo.xlsx salida
```

### Ejemplo

```bash
python split_excel.py ventas_2025.xlsx resultado
```

## Opciones

### Definir cantidad de filas por archivo

```bash
python split_excel.py archivo.xlsx salida --rows 50000
```

### Procesar una hoja específica

```bash
python split_excel.py archivo.xlsx salida --sheet "Datos"
```

### Combinando opciones

```bash
python split_excel.py archivo.xlsx salida --rows 25000 --sheet "Movimientos"
```

## Resultado

Si el archivo original contiene:

| ID | Nombre |
|----|---------|
| 1 | Juan |
| 2 | Ana |
| ... | ... |

Se generarán archivos como:

```text
archivo_parte_1.xlsx
archivo_parte_2.xlsx
archivo_parte_3.xlsx
```

Cada archivo conservará el encabezado original.

## Dependencias

- openpyxl

## Licencia

MIT License

## Autor

Proyecto de utilidad para automatización y procesamiento de archivos Excel.