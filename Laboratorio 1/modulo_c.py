from functools import wraps
from typing import Callable, Any


# C.1 – Decorador de validación
def requiere_positivos(func: Callable) -> Callable: # Callable representa un objeto que puede ser llamado (como una función)
    """
    Decorador que verifica que todos los argumentos numéricos sean > 0.
    Si alguno no lo es, lanza ValueError.
    """
    @wraps(func) # es un decorador que ayuda a preservar la metadata de la función original cuando se crea un decorador
    def wrapper(*args, **kwargs):
        # Combinar args y kwargs en un solo iterable de valores
        valores = list(args) + list(kwargs.values())
        
        # Verificar que todos los valores numéricos sean positivos
        for i, valor in enumerate(valores):
            if isinstance(valor, (int, float)) and valor <= 0:
                raise ValueError(
                    f"El argumento en la posición {i + 1} o parámetro '{valor}' debe ser mayor que 0."
                )
        
        # Si todo está bien, ejecutar la función original
        return func(*args, **kwargs)
    
    return wrapper


# Funciones decoradas
@requiere_positivos
def calcular_descuento(precio: float, porcentaje: float) -> float:
    """
    Calcula el precio final después de aplicar un descuento.
    
    Args:
        precio: Precio original
        porcentaje: Porcentaje de descuento (ej: 0.2 para 20%)
        
    Returns:
        Precio con descuento aplicado
    """
    return precio * (1 - porcentaje)

@requiere_positivos
def escala(valor: float, factor: float) -> float:
    """
    Multiplica un valor por un factor de escala.
    
    Args:
        valor: Valor original
        factor: Factor de escala (> 0)
        
    Returns:
        Valor escalado
    """
    return valor * factor


# === Pruebas ===

print("\nC.1 – Decorador de validación")
print("=== Casos válidos ===")
print("calcular_descuento(100, 0.2):", calcular_descuento(100, 0.2))
print("escala(10, 2):", escala(10, 2)) 

print("\n=== Casos con errores ===")
try:
    calcular_descuento(-1, 0.2)
except ValueError as e:
    print("calcular_descuento(-1, 0.2):", e)

try:
    calcular_descuento(100, 0)
except ValueError as e:
    print("calcular_descuento(100, 0):", e)

try:
    escala(-5, 2)
except ValueError as e:
    print("escala(-5, 2):", e)

try:
    escala(10, -1)
except ValueError as e:
    print("escala(10, -1):", e)