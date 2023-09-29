import os

def main():
    # Solicitar los datos del estudiante
    nombre = input("Ingrese su nombre: ")
    carrera = input("Ingrese su carrera: ")
    universidad = input("Ingrese su universidad: ")
    ciudad = input("Ingrese la ciudad donde estudia: ")

    # Solicitar los gastos mensuales
    alquiler = float(input("Ingrese su gasto mensual de alquiler: "))
    comida = float(input("Ingrese su gasto mensual de comida: "))
    transporte = float(input("Ingrese su gasto mensual de transporte: "))
    libros = float(input("Ingrese su gasto mensual de libros: "))
    otros = float(input("Ingrese su gasto mensual de otros: "))

    # Calcular los gastos totales
    gastos_totales = alquiler + comida + transporte + libros + otros

    # Generar el informe
    informe = f"""
    Nombre: {nombre}
    Carrera: {carrera}
    Universidad: {universidad}
    Ciudad: {ciudad}

    Gastos mensuales:
        Alquiler: ${alquiler}
        Comida: ${comida}
        Transporte: ${transporte}
        Libros: ${libros}
        Otros: ${otros}

    Gastos totales: ${gastos_totales}
    """

    # Guardar el informe
    with open(f"{nombre}.txt", "w") as f:
        f.write(informe)

if __name__ == "__main__":
    main()

