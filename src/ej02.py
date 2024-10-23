def pedirEdad():
    """
    Función para pedir la edad del usuario
    """
    return input("Introduzca su edad: ")

def validarEdad(edad):
    """
    Función para validar la edad
    """

    if not edad.isdigit():
        print("La edad tiene que ser un numero.")
        return None
    
    edad = int(edad)    

    if edad < 0:
        print("La edad debe ser mayor que 0")
        return None
    return edad
    
def mostrarEdad(edad):
    """
    Función para mostrar los años que ha cumplido (desde 1 hasta edad)
    """
    incremento = 0
    for cumplidos in range(1, edad + 1):
        incremento += 1
        print(incremento)

def main():

    # Entrada
    edad = pedirEdad()
    # Validar
    edad = validarEdad(edad)
    # Salida
    if edad is not None:
        mostrarEdad(edad)
if __name__ == '__main__':
    main()