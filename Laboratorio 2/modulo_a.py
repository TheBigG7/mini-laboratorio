import Utilidades_String as u_s

# Casos de prueba para el modulo Utilidades_String
print("1. Normalización de cadenas:")
print(u_s.normalizar_string("  PyTHon              ES  GenIaL  "))

print("\n2. Validación de emails:")
print(u_s.validar_email("contacto@empresa.es")) 
print(u_s.validar_email("invalid_email"))       

print("\n3. Formateo de teléfono (caso válido):")
print(u_s.formato_telefono("5551234567"))

# Error controlado
print("\n4. Teléfono inválido:")
try:
    print(u_s.formato_telefono("123456789")) 
except ValueError as e:
    print(f"Error capturado: {e}")  # Muestra el mensaje de error