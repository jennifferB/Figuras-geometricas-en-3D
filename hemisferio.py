import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parámetros del hemisferio
radio = 6  # Ajustar radio para que encaje con los límites deseados
resolucion = 50

# Crear una cuadrícula de ángulos theta (azimutal) y phi (polar)
theta = np.linspace(0, np.pi, resolucion)  # Ángulo polar: de 0 a π
phi = np.linspace(0, 2 * np.pi, resolucion)  # Ángulo azimutal: de 0 a 2π
theta, phi = np.meshgrid(theta, phi)

# Convertir coordenadas esféricas a cartesianas
x = radio * np.sin(theta) * np.cos(phi)
y = radio * np.sin(theta) * np.sin(phi)
z = radio * np.cos(theta)

# Crear la base circular en Z = 0
phi_base = np.linspace(0, 2 * np.pi, resolucion)
x_base = radio * np.cos(phi_base)
y_base = radio * np.sin(phi_base)
z_base = np.zeros_like(x_base)

# Crear la figura y los ejes 3D
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Dibujar la superficie del hemisferio
ax.plot_surface(x, y, z, cmap='viridis', alpha=0.8, edgecolor='k', linewidth=0.5)

# Dibujar la base circular
ax.plot(x_base, y_base, z_base, 'k-', linewidth=1.5)  # Contorno de la base
ax.plot_trisurf(x_base, y_base, z_base, color='skyblue', alpha=0.6)  # Relleno de la base con trisurf

# Configurar límites personalizados
ax.set_xlim(-7, 7)  # Eje X de -7 a 7
ax.set_ylim(-6, 6)  # Eje Y de -6 a 6
ax.set_zlim(-1, 6)   # Extiende el eje Z para incluir la base

# Etiquetas y título
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Hemisferio 3D con Base - Jenniffer", fontsize=12)

# Mostrar la figura
plt.show()
