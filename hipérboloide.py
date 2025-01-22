import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir los parámetros del hipérboloide
u = np.linspace(-2, 2, 100)
v = np.linspace(0, 2 * np.pi, 100)
u, v = np.meshgrid(u, v)

# Ecuaciones paramétricas del hipérboloide de una sola hoja
x = u * np.cos(v)
y = u * np.sin(v)
z = np.sqrt(u**2 + 1)

# Crear figura 3D
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie del hipérboloide
surf = ax.plot_surface(x, y, z, cmap='Pastel1', edgecolor='none')

# Ajustar límites
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.set_zlim(0, 3)
ax.set_box_aspect([1, 1, 1])  # Aspecto proporcional

# Títulos y etiquetas
ax.set_title("Hipérboloide 3D - Jenniffer", fontsize=12)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Mostrar barra de colores
fig.colorbar(surf)

# Mostrar figura
plt.show()
