from datetime import datetime, timedelta


def get_date_from_string(s: str):
    return datetime.strptime(s, '%Y-%m-%d')


def sobrepasa_fecha_maxima_entrega(fecha_prestamo: datetime, fecha_fin: datetime):
    fecha_maxima = fecha_prestamo + timedelta(days=30)
    if fecha_fin > fecha_maxima:
        return True
    return False