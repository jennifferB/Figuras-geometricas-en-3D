import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Parámetros del cono
radio_base = 1
altura = 2
num_puntos = 50  # Número de puntos para definir la base

# Crear coordenadas para la base del cono
theta = np.linspace(0, 2 * np.pi, num_puntos)
x_base = radio_base * np.cos(theta)
y_base = radio_base * np.sin(theta)
z_base = np.zeros_like(theta)

# Coordenadas del vértice del cono
x_vertice = 0
y_vertice = 0
z_vertice = altura

# Crear figura 3D
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Dibujar la base del cono como un polígono 3D
vertices_base = [[x, y, 0] for x, y in zip(x_base, y_base)]
poly_base = Poly3DCollection([vertices_base], color='lightblue', alpha=0.5, edgecolor='b')
ax.add_collection3d(poly_base)

# Dibujar las aristas que conectan el vértice con la base
for x, y in zip(x_base, y_base):
    ax.plot([x_vertice, x], [y_vertice, y], [z_vertice, 0], 'k-')  # Aristas negras

# Dibujar el vértice del cono
ax.scatter(x_vertice, y_vertice, z_vertice, color='red', s=50, label='Vértice')

# Ajustar límites
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(0, 2.5)
ax.set_box_aspect([1, 1, 1])  # Aspecto proporcional

# Etiquetas y título
ax.set_title("Cono 3D - Jenniffer", fontsize=12)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()

# Mostrar figura
plt.show()
