# Time 1440 Helper

Herramienta para trabajar con horarios utilizando una representación basada en minutos desde el inicio del día.

La técnica Base 1440 simplifica cálculos de duración, validaciones de rangos y turnos que cruzan medianoche.

---

# Concepto

Cada hora se convierte a minutos:

| Hora | Minutos |
|--------|--------:|
| 00:00 | 0 |
| 06:00 | 360 |
| 12:00 | 720 |
| 18:00 | 1080 |
| 24:00 | 1440 |

Ejemplo:

```text
22:00 = 1320
06:00 = 360
```

Como el rango cruza medianoche:

```text
22:00 → 1320
06:00 → 1800
```

---

# Características

- Conversión HH:MM → minutos.
- Conversión minutos → HH:MM.
- Cálculo de duración.
- Validación de horarios dentro de un rango.
- Soporte para rangos que cruzan medianoche.
- Sin dependencias externas.

---

# Uso

```bash
python time_1440.py
```

Utiliza los valores por defecto:

```text
22:00 → 06:00
```

---

## Ejemplo

```bash
python time_1440.py --start 22:00 --end 06:00 --check 02:00
```

Resultado:

```text
Inicio       : 22:00 = 1320
Fin          : 06:00 = 1800
Duración     : 480 minutos
Duración hs  : 8.00
Hora check   : 02:00
Dentro rango : SI
```

---

# Casos de uso

- Gestión de turnos.
- Horarios laborales.
- Sistemas de guardias.
- Control horario.
- Automatización de calendarios.
- Validación de asistencia.

---

# Dependencias

```txt
Standard Library Only
```

---

# Licencia

MIT License
