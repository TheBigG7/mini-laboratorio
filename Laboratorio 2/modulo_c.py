def saludar(nombre: str) -> str:
    return f"Hola, {nombre}"

edad: int = 25
altura: float = 1.75
es_estudiante: bool = True

from typing import List # proporciona soporte para type hints (sugerencias de tipo)

def obtener_nombres() -> List[str]:
    return ["Ana", "Luis", "Carlos"]

numeros: List[int] = [1, 2, 3, 4, 5]

from typing import Union

def convertir_valor(valor: str) -> Union[int, float]:
    if "." in valor:
        return float(valor)
    return int(valor)

resultado: Union[int, str] = 42  # Puede ser int o str

from typing import Optional

def encontrar_usuario(id_usuario: int) -> Optional[str]:
    if id_usuario == 1:
        return "Administrador"
    return None

usuario: Optional[str] = encontrar_usuario(2)  # Puede ser str o None
print("##########################################\n")
print("=== Pruebas de las funciones ===\n")

# Prueba de la función `saludar`
print("1. Función `saludar`: Saludamos a 'María'")
print(saludar("María")) 
print()

# Prueba de las variables con type hints
print("2. Variables con type hints:")
print(f"Edad: {edad}, Altura: {altura}, ¿Es estudiante?: {es_estudiante}")
print()

# Prueba de la función `obtener_nombres`
print("3. Función `obtener_nombres`: Lista de nombres")
print(obtener_nombres()) 
print()

# Prueba de la variable `numeros`
print("4. Variable `numeros`: Lista de números")
print(numeros) 
print()

# Prueba de la función `convertir_valor`
print("5. Función `convertir_valor`: Convertimos '42' y '3.14'")
print(convertir_valor("42"))  
print(convertir_valor("3.14")) 
print()

# Prueba de la función `encontrar_usuario`
print("6. Función `encontrar_usuario`: Buscamos usuarios con ID 1 y 2")
print(encontrar_usuario(1)) 
print(encontrar_usuario(2))  
print()

# Prueba de la variable `usuario`
print("7. Variable `usuario`: Resultado de buscar usuario con ID 2")
print(usuario) 