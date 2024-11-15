from suma import sumar
from resta import restar
from multiplicar import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def menu():
    print("Calculadora")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Suma avanzada (N números)")
    print("6. Salir")

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print("Resultado:", sumar(a, b))

    elif opcion == "2":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print("Resultado:", restar(a, b))

    elif opcion == "3":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print("Resultado:", multiplicar(a, b))

    elif opcion == "4":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print("Resultado:", dividir(a, b))

    elif opcion == "5":
        numeros = input("Ingrese los números separados por espacios: ").split()
        numeros = [float(num) for num in numeros]
        print("Resultado:", suma_avanzada(*numeros))

    elif opcion == "6":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida, intente de nuevo.")
