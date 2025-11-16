from datetime import datetime

def today(date=None):
    """Devuelve la fecha actual o formatea una fecha dada."""
    if date is None:
        return datetime.now().strftime("%d-%m-%Y")
    return date.strftime("%d-%m-%Y")
