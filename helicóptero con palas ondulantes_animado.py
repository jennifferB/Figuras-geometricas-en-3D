import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Crear la figura y el sistema de coordenadas 3D
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Definir el cuerpo principal del helicóptero (cilindro)
body_radius = 1
body_height = 4
body = ax.bar3d(0, 0, -body_height / 2, body_radius * 2, body_radius * 2, body_height, color='gray')

# Definir la cola del helicóptero (cilindro)
tail_length = 2
tail_radius = 0.2
tail = ax.bar3d(-body_radius - tail_length, 0, -tail_radius, tail_length, tail_radius * 2, tail_radius, color='gray')

# Función para dibujar las palas con movimiento ondulante
def draw_rotor(t):
    # Colores pastel para las palas
    pastel_colors = ['#FFD1DC', '#FFB6C1', '#B3E5FC', '#FFEB99']
    
    # Cálculo de la rotación de las palas
    angle = np.sin(t) * np.pi / 4  # Movimiento ondulante con función seno

    # Coordenadas para las palas
    rotor_length = 2
    rotor_width = 0.1
    
    # Dibujar 4 palas
    for i in range(4):
        # Crear palas con diferentes colores
        color = pastel_colors[i % len(pastel_colors)]
        
        # Ángulos de rotación para cada pala
        rotor_angle = angle + (i * np.pi / 2)  # Desplazamiento angular entre palas
        
        # Coordenadas de las palas con movimiento
        x_rotor = np.linspace(-rotor_length, rotor_length, 2)
        y_rotor = np.sin(rotor_angle) * np.ones_like(x_rotor)  # Movimiento ondulante en Y
        z_rotor = np.cos(rotor_angle) * np.ones_like(x_rotor)  # Movimiento ondulante en Z
        
        ax.plot(x_rotor, y_rotor, z_rotor, color=color, lw=2)  # Dibujar pala

# Función de animación
def animate(t):
    ax.clear()  # Limpiar el gráfico antes de cada actualización
    
    # Redibujar el cuerpo y la cola del helicóptero
    ax.bar3d(0, 0, -body_height / 2, body_radius * 2, body_radius * 2, body_height, color='gray')
    ax.bar3d(-body_radius - tail_length, 0, -tail_radius, tail_length, tail_radius * 2, tail_radius, color='gray')
    
    # Dibujar las palas del helicóptero
    draw_rotor(t)
    
    # Ajustar límites del gráfico
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_zlim(-3, 3)
    ax.set_title("Helicóptero 3D con palas ondulantes", fontsize=15)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

# Crear la animación
ani = FuncAnimation(fig, animate, frames=np.linspace(0, 2 * np.pi, 100), interval=50)

# Mostrar la animación
plt.show()
