"""
Utilidades para manipulación de cadenas.
"""

def normalizar_string(s: str) -> str:
    """Normaliza una cadena (minúsculas, espacios consistentes)."""
    return " ".join(s.strip().lower().split())

def validar_email(email: str) -> bool:
    """Valida formato básico de email (contiene '@' y dominio con '.')."""
    return "@" in email and "." in email.split("@")[1]