import csv
import argparse
from pathlib import Path


def repair_csv(input_file, output_file, log_file=None, delimiter=';'):
    total = 0
    correctas = 0
    errores = 0

    if log_file:
        log = open(log_file, 'w', encoding='utf-8')
    else:
        log = None

    with open(input_file, 'r', encoding='utf-8', errors='replace', newline='') as infile, \
         open(output_file, 'w', encoding='utf-8', newline='') as outfile:

        reader = csv.reader(infile, delimiter=delimiter)
        writer = csv.writer(outfile, delimiter=delimiter)

        while True:
            try:
                fila = next(reader)
                total += 1

                writer.writerow(fila)
                correctas += 1

                if total % 10000 == 0:
                    print(f"Procesadas: {total:,}")

            except StopIteration:
                break

            except Exception as e:
                errores += 1

                mensaje = f"Línea aproximada {total + 1}: {str(e)}"

                print(f"[ERROR] {mensaje}")

                if log:
                    log.write(mensaje + "\n")

                continue

    if log:
        log.close()

    print("\n========== RESUMEN ==========")
    print(f"Filas procesadas : {total:,}")
    print(f"Filas válidas    : {correctas:,}")
    print(f"Filas con error  : {errores:,}")
    print("============================")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Repara archivos CSV eliminando filas corruptas."
    )

    parser.add_argument("input_file")
    parser.add_argument("output_file")

    parser.add_argument(
        "--delimiter",
        default=';',
        help="Separador del CSV. Default: ;"
    )

    parser.add_argument(
        "--log",
        default="repair.log",
        help="Archivo de log. Default: repair.log"
    )

    args = parser.parse_args()

    repair_csv(
        input_file=args.input_file,
        output_file=args.output_file,
        log_file=args.log,
        delimiter=args.delimiter
    )