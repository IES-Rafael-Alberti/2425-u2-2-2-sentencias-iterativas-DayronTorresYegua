def entradaEntero():
    """
    Función para introducir un numero entero
    """
    return int(input("Introduce un numero entero: "))

def procesamiento(entero):
    """
    Funcion para crear un triangul con los numeros impares
    """

    for numeros in range(1, entero + 1, 2):
        fila = []
        for filas in range(numeros, 0, -2):
             fila.append(filas)
        print(" ".join(map(str, fila)))

def salida(fila):
    """
    Función para mostrar el resultado
    """

    print(fila)

def main():

    # Entrada
    entero = entradaEntero()
    # Procesamiento
    fila = procesamiento(entero)
    # Salida
    salida(fila)
if __name__ == '__main__':
    main()

