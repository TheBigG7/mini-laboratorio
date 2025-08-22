# Importaciones ABSOLUTAS (desde fuera del paquete)
from mi_paquete_mod_b.strings import validar_email
from mi_paquete_mod_b import divicion_segura  # Usa __init__.py para acceso directo

# Caso 1: Usar función del módulo 'strings' (importación absoluta)
print("Email válido?", validar_email("user@example.com"))  # True

# Caso 2: Usar función reexportada en __init__.py (importación absoluta simplificada)
print("División segura:", divicion_segura(10, 2))  # 5.0

# Caso 3: Probar importación RELATIVA dentro del paquete (via format_number_as_string)
from mi_paquete_mod_b.numbers import numero_a_string
print("Número formateado:", numero_a_string(3.1415))  
# Output: 'el resultado es 3.14' (normalizado por strings.normalize_string)