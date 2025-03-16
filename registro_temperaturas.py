# Actualizacion de codigo a Desarrollo de Función para Calcular Temperaturas Promedio en Python
def calcular_temperatura_promedio(temperaturas):
    promedios = {}
    for ciudad, temps in temperaturas.items():
        promedios[ciudad] = sum(temps) / len(temps)
    return promedios

datos_temperaturas = {
    "Quito": [15, 16, 14, 15],
    "Guayaquil": [28, 30, 29, 27],
    "Cuenca": [12, 13, 11, 14]
}

resultado = calcular_temperatura_promedio(datos_temperaturas)
print("Temperaturas promedio por ciudad:")
for ciudad, temp_promedio in resultado.items():
    print(f"{ciudad}: {temp_promedio:.2f}°C")
