def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero.")
    return a / b


# Menú interactivo
def calculadora():

    while True:
        print("\n--- CALCULADORA PYTHON ---")
        try:
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("1) Sumar  2) Restar  3) Multiplicar  4) Dividir")
            opcion = input("Elije (1-4): ")

            match opcion:
                case "1":
                    resultado = sumar(a, b)
                case "2":
                    resultado = restar(a, b)
                case "3":
                    resultado = multiplicar(a,b)
                case "4":
                    resultado = dividir(a,b)
                case "5":
                    print("Saliendo del programa")
                    break
                case _:
                    print("Opción inválida")
                    
            print(f"Resultado: {resultado}")
        except ValueError as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    calculadora()
