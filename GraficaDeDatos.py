import random
import matplotlib.pyplot as plt

def simular_galton(num_canicas, num_niveles):
    contenedores = [0] * (num_niveles + 1)

    for _ in range(num_canicas):
        posicion = 0
        for _ in range(num_niveles):
            direccion = random.choice([-1, 1])
            posicion += direccion
        contenedores[posicion] += 1

    return contenedores

def graficar_histograma(contenedores):
    num_niveles = len(contenedores)
    niveles = list(range(num_niveles))

    plt.bar(niveles, contenedores)
    plt.xlabel('Contenedores')
    plt.ylabel('Cantidad de canicas')
    plt.title('Histograma de una máquina de Galton')

    plt.show()

# Parámetros de la simulación
num_canicas = 3000
num_niveles = 12

# Simulación de la máquina de Galton
resultados = simular_galton(num_canicas, num_niveles)

# Graficar histograma
graficar_histograma(resultados)
