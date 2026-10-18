# Desafío 91: Generación de números de punto flotante
# Simulación de temperaturas aleatorias con random.uniform()

import random


def generar_temperaturas(cantidad, minimo=-10.0, maximo=40.0):
    """Genera una lista de temperaturas aleatorias en [minimo, maximo]."""
    temperaturas = []

    for _ in range(cantidad):
        temperatura = random.uniform(minimo, maximo)
        temperaturas.append(round(temperatura, 2))

    return temperaturas


def mostrar_estadisticas(temperaturas):
    """Muestra datos básicos para el análisis posterior."""
    promedio = sum(temperaturas) / len(temperaturas)

    print(f"Cantidad de datos: {len(temperaturas)}")
    print(f"Temperatura mínima: {min(temperaturas)} °C")
    print(f"Temperatura máxima: {max(temperaturas)} °C")
    print(f"Temperatura promedio: {promedio:.2f} °C")


def main():
    print("Desafío 91: Generación de temperaturas aleatorias")
    print()

    temperaturas = generar_temperaturas(10)

    print("Temperaturas generadas (°C):")
    for i, temp in enumerate(temperaturas, start=1):