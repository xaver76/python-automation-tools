# CSV Repair Tool

Herramienta para procesar archivos CSV grandes y generar una versión limpia eliminando filas corruptas.

## Características

- Procesamiento por streaming.
- Bajo consumo de memoria.
- Compatible con archivos de varios GB.
- Registro de errores en archivo de log.
- Continúa procesando aunque encuentre errores.

## Uso

python repair_csv.py origen.csv limpio.csv

## Opciones

--delimiter ","
--log errores.log