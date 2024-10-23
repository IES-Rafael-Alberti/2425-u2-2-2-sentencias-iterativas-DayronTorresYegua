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

def listaImpares(numero):
    """
    Función para mostrar los numeros impares desde 1 hasta el numero introducido
    """
    impares = []
    for numeros in range(1, numero + 1, 2):
        print(numeros, end=", ")
        impares.append(numeros)
    return impares
    
def main():

    # Entrada
    numero = pedirNumero()
    # Validar
    numero = validarNumero(numero)
    # Salida
    listaImpares(numero)
if __name__ == '__main__':
    main()