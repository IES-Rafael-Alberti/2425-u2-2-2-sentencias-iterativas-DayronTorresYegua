def tabla():
    """
    Función para crear las tablas del 1 al 10
    """
    for numero in range(1,11):
        print(f"Tabla de multiplicar del: {numero}")
        for aumento in range(1,11):
            resultado = numero * aumento
            print(f"{numero} x {aumento} = {resultado}")

def main():

    # Salida
    tabla()
if __name__ == '__main__':
    main()