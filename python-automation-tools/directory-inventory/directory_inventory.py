from pathlib import Path
from datetime import datetime
import csv
import argparse


def format_size(size_bytes):
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 ** 2:
        return f"{size_bytes / 1024:.2f} KB"
    elif size_bytes < 1024 ** 3:
        return f"{size_bytes / (1024 ** 2):.2f} MB"
    else:
        return f"{size_bytes / (1024 ** 3):.2f} GB"


def generate_inventory(input_dir, output_file):
    input_path = Path(input_dir)

    if not input_path.exists():
        print(f"La carpeta no existe: {input_path}")
        return

    total_files = 0
    total_size = 0

    with open(output_file, "w", encoding="utf-8-sig", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")

        writer.writerow([
            "ruta_completa",
            "carpeta",
            "archivo",
            "extension",
            "tamano_bytes",
            "tamano_legible",
            "fecha_modificacion"
        ])

        for file_path in input_path.rglob("*"):
            if file_path.is_file():
                try:
                    stat = file_path.stat()

                    total_files += 1
                    total_size += stat.st_size

                    writer.writerow([
                        str(file_path),
                        str(file_path.parent),
                        file_path.name,
                        file_path.suffix.lower(),
                        stat.st_size,
                        format_size(stat.st_size),
                        datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
                    ])

                    if total_files % 1000 == 0:
                        print(f"Archivos procesados: {total_files:,}")

                except Exception as e:
                    print(f"Error con archivo {file_path}: {e}")

    print("\n========== RESUMEN ==========")
    print(f"Carpeta analizada : {input_path}")
    print(f"Archivos          : {total_files:,}")
    print(f"Tamaño total      : {format_size(total_size)}")
    print(f"Archivo generado  : {output_file}")
    print("============================")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Genera un inventario CSV de archivos dentro de una carpeta."
    )

    parser.add_argument("input_dir", help="Carpeta a analizar")
    parser.add_argument("output_file", help="Archivo CSV de salida")

    args = parser.parse_args()

    generate_inventory(args.input_dir, args.output_file)