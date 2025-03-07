import random

# Definir dimensiones de la matriz
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 2  # Número de semanas a registrar

# Crear una matriz 3D que represente los datos de temperaturas diarias en varias ciudades
matriz_temperaturas = [[[random.randint(10, 30) for _ in range(len(dias_semana))] for _ in range(semanas)] for _ in range(len(ciudades))]

# Utilizar bucles anidados para calcular el promedio de temperaturas por ciudad y semana
for i in range(len(ciudades)):
    print(f"\nCiudad: {ciudades[i]}")
    for j in range(semanas):
        suma_temperaturas = sum(matriz_temperaturas[i][j])
        promedio = suma_temperaturas / len(dias_semana)
        print(f"  Semana {j + 1}: Promedio de temperatura = {promedio:.2f}°C")
