import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Crear figura 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Función para dibujar cilindros (usados para el cuerpo y las palas)
def draw_cylinder(radius, height, z_offset, color, rotation=0):
    theta = np.linspace(0, 2 * np.pi, 100)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    z = np.linspace(0, height, 100) + z_offset

    X, Y = np.meshgrid(x, z)
    Z = np.tile(y, (len(z), 1)).T
    
    ax.plot_surface(X, Y, Z, color=color, alpha=0.6)

# Cuerpo del helicóptero (cilindro principal)
draw_cylinder(2, 4, 0, 'skyblue', rotation=0)

# Cola del helicóptero (cilindro)
draw_cylinder(0.5, 2, 4, 'lightblue', rotation=0)

# Palas principales del helicóptero (cilindros más pequeños)
draw_cylinder(0.1, 1, 3.5, 'blue', rotation=45)  # Pala principal (izquierda)
draw_cylinder(0.1, 1, 3.5, 'darkblue', rotation=-45)  # Pala principal (derecha)

# Pala de cola (cilindro más delgado)
draw_cylinder(0.05, 1.5, 5, 'dodgerblue', rotation=0)

# Ajustar límites
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(0, 6)
ax.set_box_aspect([2, 2, 2])  # Aspecto proporcional

# Títulos y etiquetas
ax.set_title("Helicóptero 3D - Jenniffer", fontsize=12)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Mostrar figura
plt.show()
