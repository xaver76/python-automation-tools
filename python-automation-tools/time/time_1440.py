import argparse


MINUTES_PER_DAY = 1440


def time_to_minutes(time_str):
    """
    Convierte HH:MM a minutos desde 00:00.
    """
    hours, minutes = map(int, time_str.split(":"))
    return hours * 60 + minutes


def minutes_to_time(minutes):
    """
    Convierte minutos a HH:MM.
    """
    minutes = minutes % MINUTES_PER_DAY
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours:02d}:{mins:02d}"


def normalize_range(start_time, end_time):
    """
    Normaliza un rango horario.
    Si el final es menor o igual al inicio, cruza medianoche.
    """
    start = time_to_minutes(start_time)
    end = time_to_minutes(end_time)

    if end <= start:
        end += MINUTES_PER_DAY

    return start, end


def duration_minutes(start_time, end_time):
    """
    Calcula duración de un rango horario.
    """
    start, end = normalize_range(start_time, end_time)
    return end - start


def is_time_in_range(time_str, start_time, end_time):
    """
    Verifica si una hora está dentro de un rango.
    Soporta rangos que cruzan medianoche.
    """
    current = time_to_minutes(time_str)
    start, end = normalize_range(start_time, end_time)

    if end > MINUTES_PER_DAY and current < start:
        current += MINUTES_PER_DAY

    return start <= current < end


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Helper para trabajar horarios usando base 1440 minutos."
    )

    parser.add_argument(
            "--start",
            default="22:00",
            help="Hora inicio HH:MM (default: 22:00)"
        )

    parser.add_argument(
            "--end",
            default="06:00",
            help="Hora fin HH:MM (default: 06:00)"
    )       

    parser.add_argument(
            "--check",
            default="02:00",
            help="Hora a verificar HH:MM (default: 02:00)"
        )

    args = parser.parse_args()

    start, end = normalize_range(args.start, args.end)
    duration = duration_minutes(args.start, args.end)

    print("========== BASE 1440 ==========")
    print(f"Inicio       : {args.start} = {start}")
    print(f"Fin          : {args.end} = {end}")
    print(f"Duración     : {duration} minutos")
    print(f"Duración hs  : {duration / 60:.2f}")

    if args.check:
        result = is_time_in_range(args.check, args.start, args.end)
        print(f"Hora check   : {args.check}")
        print(f"Dentro rango : {'SI' if result else 'NO'}")

    print("===============================")