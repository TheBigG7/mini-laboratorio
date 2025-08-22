"""
Módulo para operaciones comunes con cadenas de texto.
Incluye funciones para normalización, validación y formateo.
"""

def normalizar_string(s: str) -> str:
    """
    Normaliza una cadena:
    - Elimina espacios al inicio/final.
    - Convierte a minúsculas.
    - Reemplaza múltiples espacios por uno solo.
    
    Args:
        s: Cadena de entrada.
    
    Returns:
        Cadena normalizada.
    """         # .join(lista) Une todos los elementos de la lista usando un espacio como separador
    return " ".join(s.strip().lower().split())


def validar_email(email: str) -> bool:
    """
    Valida si un email tiene formato básico:
    - Contiene '@' y un dominio con '.' (ej: usuario@dominio.com).
    
    Args:
        email: Cadena a validar.
    
    Returns:
        True si es válido, False en caso contrario.
    """
    if "@" not in email:
        return False
    # divide la cadena en una lista usando "@" como separador
    # [1] toma el segundo elemento de la lista (índice 1)
    domain = email.split("@")[1]
    return "." in domain #Retorna True si encuentra un punto, False si no


def formato_telefono(telefono: str) -> str:
    """
    Formatea un número de teléfono a estilo (365) 456-7890.
    
    Args:
        phone: Cadena con 10 dígitos numéricos.
    
    Returns:
        Cadena formateada.
    
    Raises:
        ValueError: Si la cadena no tiene 10 dígitos numéricos.
    """             # .isdigit() Verifica si una cadena contiene solo dígitos numéricos (0-9).
    if not telefono.isdigit() or len(telefono) != 10:
        raise ValueError("El teléfono debe tener 10 dígitos numéricos.")
    return f"({telefono[:3]}) {telefono[3:6]}-{telefono[6:]}"