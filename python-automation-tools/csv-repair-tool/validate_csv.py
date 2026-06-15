import csv
import argparse
from pathlib import Path


def validate_csv(input_file, delimiter=';', log_file="validate.log"):
    total = 0
    validas = 0
    errores = 0

    input_path = Path(input_file)

    with open(log_file, 'w', encoding='utf-8') as log:
        log.write(f"Validación CSV: {input_path.name}\n")
        log.write("=" * 40 + "\n")

        with open(input_file, 'r', encoding='utf-8', errors='replace', newline='') as infile:
            reader = csv.reader(infile, delimiter=delimiter)

            while True:
                try:
                    fila = next(reader)
                    total += 1

                    if total == 1:
                        columnas_base = len(fila)

                    if len(fila) != columnas_base:
                        errores += 1
                        log.write(
                            f"Línea {total}: columnas esperadas {columnas_base}, encontradas {len(fila)}\n"
                        )
                    else:
                        validas += 1

                    if total % 10000 == 0:
                        print(f"Validando: {total:,}")

                except StopIteration:
                    break

                except Exception as e:
                    errores += 1
                    log.write(f"Línea aproximada {total + 1}: {str(e)}\n")
                    continue

    print("\n========== RESUMEN ==========")
    print(f"Archivo          : {input_path.name}")
    print(f"Filas procesadas : {total:,}")
    print(f"Filas válidas    : {validas:,}")
    print(f"Filas con error  : {errores:,}")
    print(f"Log generado     : {log_file}")
    print("============================")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Valida un archivo CSV grande sin cargarlo completo en memoria."
    )

    parser.add_argument("input_file")

    parser.add_argument(
        "--delimiter",
        default=';',
        help="Separador del CSV. Default: ;"
    )

    parser.add_argument(
        "--log",
        default="validate.log",
        help="Archivo de log. Default: validate.log"
    )

    args = parser.parse_args()

    validate_csv(
        input_file=args.input_file,
        delimiter=args.delimiter,
        log_file=args.log
    )