import os

tasks = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("Presione Enter para continuar...")

def menu():
    print("Bienvenido al sistema de gestión de tareas.")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Actualizar tarea")
    print("4. Completar tarea")
    print("5. Salir")
    choice = input("Seleccione una opción: ")
    return choice

def add_task():
    print("Agregar tareas:")
    task = input("Ingrese la tarea: ")
    tasks.append(task)
    print("Tarea agregada.")

def view_tasks():
    if not tasks:
        print("No hay tareas pendientes.")
    else:
        print("Tareas pendientes:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def updated_tasks():
    try:
        if tasks:
            task_num = int(input("Ingrese el número de la tarea a actualizar: "))
            if 0 < task_num <= len(tasks):
                new_task = input("Ingrese la nueva descripción de la tarea: ")
                tasks[task_num - 1] = new_task
                print("Tarea actualizada.")
            else:
                print("Número de tarea inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")

def delete_task():
    try:
        if not tasks:
            print("No hay tareas para completar.")
            return
        task_num = int(input("Ingrese el número de la tarea a marcar como completada: "))
        if 0 < task_num <= len(tasks):
            tasks.pop(task_num - 1)
            print("Tarea completada.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")
        
def exit_program():
    print("Saliendo del programa. ¡Hasta luego!")
    return False
    
def main():
    isActive = True
    while isActive:
        clear_screen()
        choice = menu()
        match choice:
            case '1':
                clear_screen()
                add_task()
                pause()
            case '2':
                clear_screen()
                view_tasks()
                pause()
            case '3':
                clear_screen()
                view_tasks()
                updated_tasks()
                pause()
            case '4':
                clear_screen()
                view_tasks()
                delete_task()
                pause()
            case '5':
                isActive = exit_program()
            case _:
                print("Opción inválida. Intente de nuevo.")
                pause()

if __name__ == "__main__":
    main()