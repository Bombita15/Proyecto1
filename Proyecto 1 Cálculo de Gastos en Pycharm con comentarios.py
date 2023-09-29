# Importar el módulo os para crear el archivo de texto
import os

# Función principal
def main():

    # Solicitar los datos del estudiante
    # Comentario: Solicita el nombre del estudiante
    nombre = input("Ingrese su nombre: ")
    # Comentario: Solicita la carrera del estudiante
    carrera = input("Ingrese su carrera: ")
    # Comentario: Solicita la universidad del estudiante
    universidad = input("Ingrese su universidad: ")
    # Comentario: Solicita la ciudad donde estudia el estudiante
    ciudad = input("Ingrese la ciudad donde estudia: ")

    # Solicitar los gastos mensuales
    # Comentario: Solicita el gasto mensual de alquiler
    alquiler = float(input("Ingrese su gasto mensual de alquiler: "))
    # Comentario: Solicita el gasto mensual de comida
    comida = float(input("Ingrese su gasto mensual de comida: "))
    # Comentario: Solicita el gasto mensual de transporte
    transporte = float(input("Ingrese su gasto mensual de transporte: "))
    # Comentario: Solicita el gasto mensual de libros
    libros = float(input("Ingrese su gasto mensual de libros: "))
    # Comentario: Solicita el gasto mensual de otros
    otros = float(input("Ingrese su gasto mensual de otros: "))

    # Calcular los gastos totales
    # Comentario: Calcula el total de los gastos mensuales
    gastos_totales = alquiler + comida + transporte + libros + otros

    # Generar el informe
    # Comentario: Crea un string con el informe del estudiante
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
    # Comentario: Abre el archivo de texto en modo de escritura
    with open(f"{nombre}.txt", "w") as f:
        # Comentario: Escribe el informe en el archivo de texto
        f.write(informe)

# Comentario: Ejecuta la función principal
if __name__ == "__main__":
    main()


