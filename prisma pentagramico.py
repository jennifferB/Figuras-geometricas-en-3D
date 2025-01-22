import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Función para generar un pentagrama en 3D
def generar_pentagrama(radio, centro_z):
    angulos = np.linspace(0, 2 * np.pi, 10, endpoint=False)
    puntos = []
    for i in range(10):
        r = radio if i % 2 == 0 else radio / 2.5  # Alternar entre radio grande y pequeño
        x = r * np.cos(angulos[i])
        y = r * np.sin(angulos[i])
        puntos.append((x, y, centro_z))
    return puntos

# Generar puntos para las bases superior e inferior
radio_base = 2
altura_prisma = 3
base_inferior = generar_pentagrama(radio_base, 0)
base_superior = generar_pentagrama(radio_base, altura_prisma)

# Crear las caras del prisma
caras = []

# Conexión de las bases
for i in range(10):
    caras.append([base_inferior[i], base_inferior[(i + 1) % 10], base_superior[(i + 1) % 10], base_superior[i]])

# Agregar las bases inferior y superior
caras.append(base_inferior)
caras.append(base_superior)

# Crear la figura 3D
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Dibujar las caras del prisma
for cara in caras:
    poly = Poly3DCollection([cara], alpha=0.7, edgecolor='k', linewidths=1)
    poly.set_facecolor('lightblue')
    ax.add_collection3d(poly)

# Ajustar límites
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(0, 4)
ax.set_box_aspect([1, 1, 1])  # Aspecto proporcional

# Etiquetas y título
ax.set_title("Prisma Pentagrámico 3D - Jenniffer", fontsize=12)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Mostrar la figura
plt.show()
