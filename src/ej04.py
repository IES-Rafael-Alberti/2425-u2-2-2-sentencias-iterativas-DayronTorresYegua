def pedirNumero():
    """
    Función que pide al usuario un numero
    """
    return input("Introduzca un numero entero positivo: ")

def validarNumero(numero):
    """
    Función para validar que el numero es entero y positivo
    """
    
    while not (numero.isdigit() and int(numero) > 0):
        print("Debe introducir un numero entero posotivo.")
        numero = pedirNumero()
    return int(numero)

def cuentaAtras(numero):
    """
    Función para mostrar la cuenta atras desde el numero introducido hasta cero
    """
    for numeros in range(1, numero + 1, + 1,):
        print(numeros, end=", ")

def main():

    # Entrada
    numero = pedirNumero()
    # Validar
    numero = validarNumero(numero)
    # Salida
    cuentaAtras(numero)
if __name__ == '__main__':
    main()