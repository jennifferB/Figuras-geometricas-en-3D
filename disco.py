import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Definir los parámetros del disco
r = 3  # Radio del disco
theta = np.linspace(0, 2 * np.pi, 100)  # Ángulo en el plano xy
z = 0  # El disco estará en el plano z = 0

# Convertir las coordenadas polares a cartesianas
x = r * np.cos(theta)
y = r * np.sin(theta)

# Crear figura 3D
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Crear un disco 3D (Polígono en el plano XY, con un pequeño grosor en Z)
verts = [list(zip(x, y, np.zeros_like(x)))]  # Círculo en Z=0
verts_upper = [list(zip(x, y, np.full_like(x, 0.5)))]  # Superficie superior del disco

# Graficar la superficie inferior (en Z=0)
ax.add_collection3d(Poly3DCollection(verts, color='lightblue', alpha=0.6))
# Graficar la superficie superior (en Z=0.5)
ax.add_collection3d(Poly3DCollection(verts_upper, color='lightgreen', alpha=0.6))

# Agregar el contorno del disco en Z=0
ax.plot(x, y, np.zeros_like(x), 'k-', linewidth=1.5)  # Contorno inferior

# Ajustar límites
ax.set_xlim(-r-1, r+1)
ax.set_ylim(-r-1, r+1)
ax.set_zlim(0, 0.6)
ax.set_box_aspect([1, 1, 0.5])  # Aspecto proporcional

# Títulos y etiquetas
ax.set_title("Platón 3D - Jenniffer", fontsize=12)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Mostrar figura
plt.show()
