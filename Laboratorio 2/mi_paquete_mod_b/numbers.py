"""
Utilidades para operaciones numéricas.
"""

# Importación RELATIVA a otro módulo del mismo paquete
from .strings import normalizar_string

def divicion_segura(a: float, b: float) -> float:
    """Divide dos números de forma segura (maneja división por cero)."""
    if b == 0:
        raise ValueError("División por cero no permitida.")
    return a / b

def numero_a_string(numero: float) -> str:
    """
    Formatea un número como cadena y lo normaliza usando una función del módulo 'strings'.
    Ejemplo de uso de importación RELATIVA dentro del paquete.
    """
    raw_string = f"El resultado es {numero:.2f}"
    return normalizar_string(raw_string)  # ¡Uso de la función importada!