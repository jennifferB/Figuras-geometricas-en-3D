import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

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

# Función para actualizar la superficie en cada fotograma
def update(frame):
    Z = np.sin(X + frame * 0.1) * np.cos(Y + frame * 0.1)  # Haciendo que las ondas se muevan
    ax.clear()  # Limpiar la figura anterior

    # Volver a graficar la superficie con el nuevo Z
    surf = ax.plot_surface(X, Y, Z, cmap='coolwarm', edgecolor='none')

    # Actualizar el título y las etiquetas
    ax.set_title("Superficie Paramétrica - Silla de Montar en Movimiento", fontsize=15)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    
    # Ajustar límites
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)
    
    return surf,

# Crear la animación
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=False)

# Mostrar la animación
plt.show()
