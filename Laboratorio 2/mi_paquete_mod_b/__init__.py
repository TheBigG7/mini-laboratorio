"""
Inicialización del paquete my_utils.
Reexporta funciones clave para simplificar las importaciones.
"""

# Reexportamos funciones importantes para acceso directo desde el paquete
from .strings import normalizar_string
from .numbers import divicion_segura

# Define qué se expone al importar el paquete
# Esto permite importar directamente desde mi_paquete_mod_b sin necesidad de especificar los módulos internos
__all__ = ["normalizar_string", "divicion_segura"]