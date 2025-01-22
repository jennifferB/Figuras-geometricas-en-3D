import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parámetros del cilindro
radio_exterior = 6  # Radio exterior
radio_interior = 4  # Radio interior
altura = 10  # Altura del cilindro
resolucion = 100  # Resolución de la malla

# Crear una cuadrícula de ángulos y alturas
theta = np.linspace(0, 2 * np.pi, resolucion)  # Ángulo azimutal: de 0 a 2π
z = np.linspace(0, altura, resolucion)  # Altura del cilindro: de 0 a altura
theta, z = np.meshgrid(theta, z)

# Coordenadas del cilindro exterior
x_exterior = radio_exterior * np.cos(theta)
y_exterior = radio_exterior * np.sin(theta)

# Coordenadas del cilindro interior
x_interior = radio_interior * np.cos(theta)
y_interior = radio_interior * np.sin(theta)

# Crear la figura y los ejes 3D
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Dibujar el cilindro exterior
ax.plot_surface(x_exterior, y_exterior, z, color='skyblue', alpha=0.6)

# Dibujar el cilindro interior (hacemos la "resta" visual al ponerlo en el interior)
ax.plot_surface(x_interior, y_interior, z, color='white', alpha=1)

# Configurar límites personalizados
ax.set_xlim(-7, 7)  # Eje X de -7 a 7
ax.set_ylim(-7, 7)  # Eje Y de -7 a 7
ax.set_zlim(0, altura)  # Altura del cilindro

# Etiquetas y título
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Cilindro Hueco 3D - Jenniffer", fontsize=12)

# Mostrar la figura
plt.show()
