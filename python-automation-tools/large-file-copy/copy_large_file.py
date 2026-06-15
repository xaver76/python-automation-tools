from pathlib import Path
import argparse
import time


def copy_large_file(source, destination, chunk_size=1024 * 1024 * 10):
    source = Path(source)
    destination = Path(destination)

    total_size = source.stat().st_size
    copied = 0

    start_time = time.time()

    with open(source, "rb") as src:
        with open(destination, "wb") as dst:

            while True:
                chunk = src.read(chunk_size)

                if not chunk:
                    break

                dst.write(chunk)

                copied += len(chunk)

                percent = (copied / total_size) * 100

                print(
                    f"\rCopiado: {copied:,} / {total_size:,} bytes "
                    f"({percent:.2f}%)",
                    end=""
                )

    elapsed = time.time() - start_time

    print("\n")
    print("=" * 50)
    print("Copia finalizada")
    print(f"Origen      : {source}")
    print(f"Destino     : {destination}")
    print(f"Tamaño      : {total_size:,} bytes")
    print(f"Tiempo      : {elapsed:.2f} segundos")
    print("=" * 50)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Copia archivos grandes mostrando progreso."
    )

    parser.add_argument("source")
    parser.add_argument("destination")

    args = parser.parse_args()

    copy_large_file(
        args.source,
        args.destination
    )