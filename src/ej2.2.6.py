def entradaEntero():
    """
    Función para introducir un numero entero
    """
    return int(input("Introduce un numero entero: "))

def procesamiento(entero):
    """
    Funcion para cambiar el numero entero por un triangulo rectangulo
    """
    triangulo = ""
    for cambio in range(1, entero):
        triangulo += "*" * cambio + "\n"
    return triangulo

def salida(triangulo):
    """
    Función para mostrar el resultado
    """

    print(triangulo)

def main():

    # Entrada
    entero = entradaEntero()
    # Procesamiento
    triangulo = procesamiento(entero)
    # Salida
    salida(triangulo)
if __name__ == '__main__':
    main()