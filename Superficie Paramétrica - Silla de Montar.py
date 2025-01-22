import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Crear la figura y el sistema de coordenadas 3D
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Definir el rango de los parámetros u y v
u = np.linspace(-2, 2, 100)
v = np.linspace(-2, 2, 100)
U, V = np.meshgrid(u, v)

# Definir la ecuación paramétrica de la silla de montar
X = U
Y = V
Z = X**2 - Y**2  # Ecuación para una silla de montar

# Aplicar colores acordes (usaremos un mapa de colores pastel)
ax.plot_surface(X, Y, Z, cmap='coolwarm', edgecolor='none')

# Títulos y etiquetas
ax.set_title("Superficie Paramétrica - Silla de Montar", fontsize=15)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Ajustar límites
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-4, 4)

# Mostrar la figura
plt.show()
