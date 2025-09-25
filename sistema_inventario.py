"""Ejercicio: Sistema de Inventario de Videojuegos
Enunciado:
Desarrolla un sistema simple para gestionar una colección personal de videojuegos. El sistema debe permitir agregar juegos, ver la colección, marcar juegos como completados y mostrar estadísticas básicas.
Requisitos Técnicos Específicos:
Tipos de Datos Obligatorios:

Listas: Para almacenar la colección de videojuegos
Tuplas: Para representar cada juego (nombre, género, estado_completado)
Strings: Para nombres de juegos y géneros
Booleanos: Para el estado de completado (True/False)
Enteros: Para números de opciones del menú y contadores

Operadores Requeridos:

Aritméticos: +, - (para contadores y cálculos)
Comparación: ==, <=, >= (para validaciones)
Lógicos: and, or, not (para condiciones)
Pertenencia: in (para verificar elementos en listas)

Estructuras de Control Obligatorias:

Condicionales: if, elif, else (mínimo 3 usos diferentes)
Bucle while: Para el menú principal del programa
Bucle for: Para iterar sobre la colección de juegos
Enumerate: Para mostrar números de índice

Funciones Requeridas (mínimo 6):

menu() - Mostrar opciones y retornar elección
add_game() - Agregar nuevo juego
view_games() - Mostrar colección completa
complete_game() - Marcar juego como completado
show_stats() - Mostrar estadísticas
main() - Función principal

Validaciones Obligatorias:

Verificar que la lista no esté vacía antes de mostrar
Validar números de opciones del menú
Controlar índices de la lista al marcar juegos

Funcionalidades Requeridas:

Agregar juego: Solicitar nombre y género, crear tupla, agregar a lista
Ver colección: Mostrar todos los juegos con estado visual (✓/✗)
Marcar completado: Seleccionar juego por número y cambiar estado
Estadísticas: Contar total, completados y pendientes usando bucles
Control de flujo: Menú que se repita hasta seleccionar salir

Elementos Adicionales:

Usar os.system() para limpiar pantalla
Función pause() con input() para control de flujo
Mensajes informativos claros para el usuario

Tiempo estimado: 50 minutos
Nivel: Básico-Intermedio"""

import os

# Lista global para juegos
juegos = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    pass

def menu():
    print("----Bienvenido Al Inventario de Videojuegos")
    print("1. Agregar un Juego")
    print("2. Ver Coleccion")
    print("3. Marcar Completado")
    print("4. Estadisticas")
    print("0. Salir")
    print("-------------------------------------------")
    pass

def add_game():
    clear_screen()
    print("----Agregar Juegos----")
    nombre = input("Ingrese el nombre del juego: ")
    genero = input("Ingrese el genero del juego: ")
    estado = (input("El juego esta completado? (si/no)"))
    
    game = (nombre, genero, estado)
    
    juegos.append(game)
    # Crear tupla (nombre, genero, False)
    # Usar append() en lista
    pass

def view_games():
    if not juegos:
        print("NO HAY JUEGOS PARA VER")
    # Usar if not para verificar lista vacía
    # Usar for con enumerate()
    # Desempaquetar tupla
    pass

def complete_game():
    # Usar if not para lista vacía
    # Usar >= y <= para validar índice
    # Modificar tupla en lista
    pass

def show_stats():
    # Usar for para contar
    # Operadores aritméticos
    pass

def main():
    isActive = True
    while isActive:
        menu()
        opcion = int(input("Ingresa una opcion: "))
        match opcion:
            case 1:
                add_game()
                print(juegos)
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 0:
                pass
            case _:
                pass
    # Usar while con booleano
    # Usar if/elif/else para opciones
    

if __name__ == "__main__":
    main()