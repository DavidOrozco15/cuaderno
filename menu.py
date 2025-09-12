import os

def menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Factorial")
    print("4. Combinatorias")
    print("5. Triángulo de Pascal")
    print("6. Celsius a Fahrenheit")
    print("7. Fahrenheit a Celsius")
    print("8. Salir")

def suma(num1, num2):
    resultado = num1 + num2
    return resultado

def resta(num1, num2):
    resultado = num1 - num2
    return resultado

def factorial(num):
    if num < 0:
        return -1
    elif num == 0:
        return 1
    else:
        f = 1
        for i in range(1, num+1):
            f = f * i
        
        return f
    
def combinatoria(n, k):
    resultado = factorial(n) // (factorial(k) * factorial(n - k))
    return resultado

def trianguloPascal(n):
    if n < 1:
        print("No se puede calcular")
    else:
        for fila in range(n):
            for col in range(fila + 1):
                print(combinatoria(fila, col), end=" ")
            print("")

def conversorFarenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def conversorCelsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def validacion(mensaje):
    valido = False
    while not valido:
        valor = input(mensaje)
        es_numero = True

        for c in valor:
            if not (c >= '0' and c <= '9'):
                es_numero = False

        if es_numero and valor != "" and int(valor) >= 0:
            valido = True
        else:
            print("Entrada inválida. Ingrese un número entero positivo.")

    return int(valor)

isActive = True
while isActive:
    menu()
    opcion = validacion("Seleccione una opción: ")

    if opcion == 1:
        os.system("clear")
        print("Suma")
        num1 = validacion("Ingrese el primer número: ")
        num2 = validacion("Ingrese el segundo número: ")
        print(f"La suma es: {suma(num1, num2)}")
        input("Presione enter para salir al menú")
        os.system("clear")

    elif opcion == 2:
        os.system("clear")
        print("Resta")
        num1 = validacion("Ingrese el primer número: ")
        num2 = validacion("Ingrese el segundo número: ")
        print(f"La resta es: {resta(num1, num2)}")
        input("Presione enter para salir al menú")
        os.system("clear")

    elif opcion == 3:
        os.system("clear")
        print("Factorial")
        num = validacion("Ingrese un número: ")
        if factorial(num) == -1:
            print("No se puede calcular el factorial de un número negativo")
        else:
            print(f"El factorial de {num} es: {factorial(num)}")
        input("Presione enter para salir al menú")
        os.system("clear")

    elif opcion == 4:
        os.system("clear")
        print("Combinatoria")
        n = validacion("Ingrese n: ")
        k = validacion("Ingrese k: ")
        if k > n:
            print("No se puede calcular")
        else:
            print(f"La combinatoria de {n} y {k} es: {combinatoria(n, k)}")
        input("Presione enter para salir al menú")
        os.system("clear")

    elif opcion == 5:
        os.system("clear")
        print("Triángulo de Pascal")
        n = validacion("Ingrese el número de filas: ")
        trianguloPascal(n)
        input("Presione enter para salir al menú")
        os.system("clear")

    elif opcion == 6:
        os.system("clear")
        print("Celsius a Fahrenheit")
        celsius = validacion("Ingrese la temperatura en Celsius: ")
        print(f"{celsius}°C son {conversorFarenheit(celsius)}°F")
        input("Presione enter para salir al menú")
        os.system("clear")

    elif opcion == 7:
        os.system("clear")
        print("Fahrenheit a Celsius")
        fahrenheit = validacion("Ingrese la temperatura en Fahrenheit: ")
        print(f"{fahrenheit}°F son {conversorCelsius(fahrenheit)}°C")
        input("Presione enter para salir al menú")
        os.system("clear")

    elif opcion == 8:
        os.system("clear")
        print("Saliendo...")
        isActive = False

    else:
        print("Opción no válida")
        input("Presione enter para volver a intentarlo")
