# Mini Laboratorio de Programación Orientada a Objetos

Este repositorio contiene una serie de ejercicios y prácticas de laboratorio para la materia de Programación Orientada a Objetos.

## Estructura del Repositorio

El repositorio está organizado en los siguientes directorios:

### Laboratorio 1

Contiene los primeros ejercicios del curso.

*   `modulo_a.py`: Funciones y Métodos
*   `modulo_b.py`: Muestra el manejo de errores y excepciones personalizadas.
*   `modulo_c.py`: Implementa decoradores, generadores y administradores de contexto.

### Laboratorio 2

Contiene ejercicios más avanzados, incluyendo la creación de paquetes.

*   `modulo_a.py`: Contiene casos de prueba para el módulo `Utilidades_String`.
*   `modulo_b.py`: (Paquetes) Ejemplifica el uso de importaciones absolutas y relativas de un paquete.
*   `modulo_c.py`: Muestra el uso de "type hints" en Python.
*   `Utilidades_String.py`: Provee funciones para normalizar, validar y formatear cadenas de texto para el `modulo_a.py`.
*   `mi_paquete_mod_b/`: Paquete que contiene módulos para operaciones con cadenas de texto y números para el `modulo_b.py`.
    *   `__init__.py`: Inicializa el paquete y reexporta funciones.
    *   `numbers.py`: Contiene funciones para operaciones numéricas.
    *   `strings.py`: Contiene funciones para manipulación de cadenas de texto.
