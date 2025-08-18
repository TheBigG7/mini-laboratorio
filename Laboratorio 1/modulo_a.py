def saludar(nombre):
    print(f"Hola, {nombre}! Bienvenido al Centro de Comandos.")
    
def despedir(nombre):
    print(f"Adiós, {nombre}! Gracias por usar el Centro de Comandos.")
    
def aplaudir(nombre):
    print(f"{nombre} aplaude con entusiasmo. ¡Buen trabajo!")
    
acciones = {
    "saludar": saludar,
    "despedir": despedir,
    "aplaudir": aplaudir
}
# No es necesario usar **kwargs en este caso, pero se incluye para demostrar   flexibilidad.
def ejecutar(accion, *args, **kwargs):
    if accion in acciones:
        funcion = acciones[accion]
        return funcion(*args, **kwargs)
    else:
        return "Acción no reconocida."
    
print(ejecutar("saludar", "Ana"))
print(ejecutar("despedir", "Luis"))
print(ejecutar("aplaudir", "Carlos"))
print(ejecutar("cantar", "Carlos"))