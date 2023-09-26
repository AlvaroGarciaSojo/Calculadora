#!C:\Users\zx20student197\AppData\Local\Programs\Python\Python311\python.exe

def sumar(x, y):
    return x + y

while True:
    print("Opciones:")
    print("Ingrese 'sumar' para sumar dos números")
    print("Ingrese 'salir' para finalizar el programa")
    user_input = input(": ")

    if user_input == "salir":
        break
    elif user_input in ("suma"):
        x = float(input("Ingrese el primer número: "))
        y = float(input("Ingrese el segundo número: "))

        if user_input == "suma":
            print(suma(x, y))
    else:
        print("Entrada no válida")
