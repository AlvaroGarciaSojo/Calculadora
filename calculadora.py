#!C:\Users\zx20student197\AppData\Local\Programs\Python\Python311\python.exe

def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

while True:
    print("Opciones:")
    print("Ingrese 'sumar' para sumar dos números")
    print("Ingrese 'resta' para restar dos números")
    print("Ingrese 'multiplica' para multiplicar dos números")
    print("Ingrese 'divide' para multiplicar dos números")
    print("Ingrese 'salir' para finalizar el programa")
    user_input = input(": ")

    if user_input == "salir":
        break
    elif user_input in ("suma", "resta", "multiplica"):
        x = float(input("Ingrese el primer número: "))
        y = float(input("Ingrese el segundo número: "))

        if user_input == "sumar":
            print(suma(x, y))
        elif user_input == "resta":
            print(resta(x, y))
        elif user_input == "multiplica":
            print(multiplica(x, y))
        elif user_input == "divide":
            print(multiplica(x, y))
    else:
        print("Entrada no válida")
