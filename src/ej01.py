def pedirPalabra():
    """
    Función que pedirá al usuario una palabra
    """
    return input("Introduzca una palabra: ")

def validarPalabra(palabra):
    """
    Función para validar que es una palabra
    """    
    if not palabra.isalpha():
        print("Solo se permiten letras.")
        return None
    else: 
        return palabra


def mostrarPalabra(palabra):
    """Función que mostrará por pantalla la palabra 10 veces
    """
    for palabras in range(10):
        print(palabra)

def main():

    # Entrada
    palabra = pedirPalabra()
    # Validar
    palabra = validarPalabra(palabra)
    # Salida
    if palabra is not None:
        mostrarPalabra(palabra)

if __name__ == '__main__':
    main()