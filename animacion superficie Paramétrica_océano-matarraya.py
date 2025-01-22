import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import matplotlib.cm as cm

# Crear la figura y el sistema de coordenadas 3D
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Definir el rango de los parámetros u y v
u = np.linspace(-2, 2, 100)
v = np.linspace(-2, 2, 100)
U, V = np.meshgrid(u, v)

# Definir la ecuación paramétrica de la silla de montar (mantarraya)
X = U
Y = V

# Función para actualizar la superficie en cada fotograma
def update(frame):
    Z = np.sin(X + frame * 0.1) * np.cos(Y + frame * 0.1)  # Movimiento de la silla

    ax.clear()  # Limpiar la figura anterior

    # Colores realistas para la mantarraya
    mantarraya_cmap = cm.Greys  # Usamos tonos de gris para representar una mantarraya real

    # Crear la mantarraya (silla de montar)
    surf = ax.plot_surface(X, Y, Z, cmap=mantarraya_cmap, edgecolor='none')

    # Añadir el fondo del océano (color de cielo)
    ax.set_facecolor('#87CEEB')  # Color de cielo azul claro

    # Crear la cola de la mantarraya (línea recta)
    # Parámetros para la cola
    t = np.linspace(0, 3, 100)  # El rango de la cola, ajustado para que esté más largo
    X_col = np.ones_like(t) * 1.5  # Colocamos la cola en la parte trasera de la mantarraya
    Y_col = np.zeros_like(t)  # Mantener la cola en el eje Y
    Z_col = np.linspace(0.1, -0.3, 100) + np.sin(frame * 0.1) * 0.2  # Movimiento ondulante en Z

    # Movimiento en el tiempo para la cola (línea recta)
    ax.plot(X_col, Y_col - 1.5, Z_col, color="gray", lw=2)  # Traza de la cola de la mantarraya

    # Actualizar el título y las etiquetas
    ax.set_title("Mantarraya Ondulante con Cola Realista", fontsize=15)
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

