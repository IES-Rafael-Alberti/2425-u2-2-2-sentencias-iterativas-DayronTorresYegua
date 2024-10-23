def entradaDatos():
    """
    Función para introducir la cantidad a invertir, el interes anual y el numero de años
    """
    cantidad = float(input("Introduzca la cantidad a invertir: "))
    interesAnual = float(input("Introduzca lel interes anual en porcentaje: "))
    años = int(input("Introduzca el numero de años de la inversion: "))

    return cantidad, interesAnual, años

def capitalObtenido(cantidad, interesAnual, años):
    """
    Función para el capital obtenido cada año
    """
    resultados = []
    for año in range(1, años + 1):
        cantidad *= 1 + interesAnual / 100
        resultados.append((año, round(cantidad, 2)))
    return resultados

def salidaDatos(resultados):
    """
    Funcion para mostar los resultados de cada año
    """
    for año, capital in resultados:
        print(f"Año {año}: {capital}")

def main():

    # Entrada
    cantidad, interesAnual, años = entradaDatos()
    # Procesamiento
    resultados = capitalObtenido(cantidad, interesAnual, años)
    # Salida
    salidaDatos(resultados)
if __name__ == '__main__':
    main()