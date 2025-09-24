import os
pendientes = []
os.system("clear")
isActive = True
while isActive:
    os.system("clear")
    print("Bienvenido a Lista de Pendientes")
    print("1. Consultar tareas")
    print("2. Añadir Tareas")
    print("3. Actualizar Tarea")
    print("4. Completar tarea")
    print("0. Salir")
    opcion = int(input("Ingresa la Opcion: "))
    match opcion:
        case 1:
            os.system("clear")
            if len(pendientes)==0:
                print("No tiene tareas pendientes")
                input("Presiona enter para continuar....")
            elif len(pendientes)>=1:
                print("Sus tareas pendientes son: ")
                for indice, tarea in enumerate(pendientes):
                    print(f"[{indice}] {tarea}")
                input("Presiona enter para continuar....")
            else:
                pass
        case 2:
            os.system("clear")
            print("Agregar Tareas")
            pendientes.append(input("Ingrese la nueva tarea: "))
            print(f"Ahora sus tareas pendientes son: {pendientes}")
            input("Presiona enter para continuar....")
        case 3:
            pass
        case 4:
            os.system("clear")
            print("Completar Tareas")
            print("Sus tareas pendientes son: ")
            for indice, tarea in enumerate(pendientes):
                print(f"[{indice}] {tarea}")
            completado = pendientes.pop(int(input("Ingrese el numero de la tarea que desea completar: ")))
            print(f"La tarea {completado} fue completada con exito")
            print(f"La lista actualizada es: {pendientes}")
            input("Presiona enter para continuar....")
        case 0:
            print("Gracias por usar el programa.")
            isActive = False
        case _:
            pass