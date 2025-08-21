# B.1 – Validación de entrada
def parsear_enteros(entradas: list[str]) -> tuple[list[int], list[str]]:
    """
    Convierte una lista de strings a enteros, capturando errores.
    
    Args:
        entradas: Lista de strings que se intentarán convertir
        
    Returns:
        Tupla con (valores_convertidos, lista_de_errores)
    """
    valores = []
    errores = []
    
    for i, entrada in enumerate(entradas):
        try:
            numero = int(entrada)
            valores.append(numero)
        except ValueError:
            # Si no se puede convertir, guardamos el error
            errores.append(f"Error en posición {i}: '{entrada}' no es un número válido")
        except Exception as e:
            # Para cualquier otro error inesperado
            errores.append(f"Error inesperado en posición {i} con '{entrada}': {str(e)}")
    
    return (valores, errores)

entradas1 = ["10", "x", "3"]
valores, errores = parsear_enteros(entradas1)
print("B.1 – Validación de entrada")
print("Entradas:", entradas1)
print("Valores convertidos:", valores)
print("Errores:", errores)
print()

# B.2 – Excepciones personalizadas y raise
# Excepción personalizada
class CantidadInvalida(Exception):
    """Excepción lanzada cuando la cantidad es inválida (<= 0)"""
    def __init__(self, mensaje="La cantidad debe ser mayor que 0"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def calcular_total(precio_unitario: float, cantidad: int) -> float:
    """
    Calcula el total de una compra.
    
    Args:
        precio_unitario: Precio de cada unidad
        cantidad: Número de unidades
        
    Returns:
        float: Total de la compra
        
    Raises:
        CantidadInvalida: Si cantidad <= 0
        ValueError: Si precio_unitario < 0
    """
    # Validar cantidad
    if cantidad <= 0:
        # raise Interrumpe el flujo normal del programa Puede lanzar una excepción predefinida (como ValueError, TypeError, etc.) o una personalizada
        raise CantidadInvalida(f"Cantidad inválida: {cantidad}. Debe ser mayor que 0")
    
    # Validar precio
    if precio_unitario < 0:
        raise ValueError(f"Precio inválido: {precio_unitario}. No puede ser negativo")
    
    # Calcular y devolver total
    return precio_unitario * cantidad

# Función para manejar las excepciones (punto de llamada)
def procesar_compra(precio_unitario: float, cantidad: int) -> str:
    """
    Procesa una compra y maneja las excepciones.
    """
    try:
        total = calcular_total(precio_unitario, cantidad)
        return f"Total calculado: ${total:.2f}"
    except CantidadInvalida as e:
        return f"Error de cantidad: {e}"
    except ValueError as e:
        return f"Error de precio: {e}"
    except Exception as e:
        return f"Error inesperado: {e}"

print("B.2 – Excepciones personalizadas y raise")
print("=== Casos válidos ===")
print(procesar_compra(10, 3))      # Debe dar: Total calculado: $30.00
print(procesar_compra(15.50, 2))   # Debe dar: Total calculado: $31.00
print(procesar_compra(100, 1))     # Debe dar: Total calculado: $100.00

print("\n=== Casos con errores ===")
print(procesar_compra(10, 0))      # Debe lanzar CantidadInvalida
print(procesar_compra(10, -5))     # Debe lanzar CantidadInvalida
print(procesar_compra(-10, 3))     # Debe lanzar ValueError
print(procesar_compra(-5, -2))     # Debe lanzar ValueError (se captura el primero)