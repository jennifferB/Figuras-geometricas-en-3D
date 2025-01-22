import matplotlib.pyplot as plt
import numpy as np

# Parámetros del toroide
radio_principal = 2  # Radio del círculo principal (distancia desde el centro del toro al centro del tubo)
radio_tubo = 0.5     # Radio del tubo (grosor del toro)
num_puntos = 100     # Número de divisiones para theta y phi

# Coordenadas paramétricas
theta = np.linspace(0, 2 * np.pi, num_puntos)
phi = np.linspace(0, 2 * np.pi, num_puntos)
theta, phi = np.meshgrid(theta, phi)

# Ecuaciones paramétricas del toroide
x = (radio_principal + radio_tubo * np.cos(phi)) * np.cos(theta)
y = (radio_principal + radio_tubo * np.cos(phi)) * np.sin(theta)
z = radio_tubo * np.sin(phi)

# Crear la figura y los ejes 3D
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Dibujar la superficie del toroide
ax.plot_surface(x, y, z, cmap='viridis', edgecolor='k', alpha=0.8)

# Ajustar los límites
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(-1, 1)
ax.set_box_aspect([1, 1, 0.5])  # Aspecto proporcional

# Etiquetas y título
ax.set_title("Toroide 3D - Jenniffer", fontsize=12)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Mostrar figura
plt.show()
