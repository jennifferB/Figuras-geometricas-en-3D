import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Coordenadas 3D de los vértices de un octaedro
puntos = {
    "P1": (1, 0, 0),  # Vértice en X positivo
    "P2": (-1, 0, 0), # Vértice en X negativo
    "P3": (0, 1, 0),  # Vértice en Y positivo
    "P4": (0, -1, 0), # Vértice en Y negativo
    "P5": (0, 0, 1),  # Vértice en Z positivo
    "P6": (0, 0, -1)  # Vértice en Z negativo
}

# Conexiones entre los puntos para formar las aristas del octaedro
conexiones = [
    ("P1", "P3"), ("P1", "P4"), ("P1", "P5"), ("P1", "P6"),
    ("P2", "P3"), ("P2", "P4"), ("P2", "P5"), ("P2", "P6"),
    ("P3", "P5"), ("P3", "P6"),
    ("P4", "P5"), ("P4", "P6")
]

# Crear figura 3D
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Graficar puntos
for nombre, coord in puntos.items():
    ax.scatter(*coord, label=nombre, s=50)  # Dibujar puntos
    ax.text(coord[0] + 0.1, coord[1] + 0.1, coord[2], nombre, fontsize=10)  # Etiquetas

# Dibujar conexiones
for p1, p2 in conexiones:
    x_coords = [puntos[p1][0], puntos[p2][0]]
    y_coords = [puntos[p1][1], puntos[p2][1]]
    z_coords = [puntos[p1][2], puntos[p2][2]]
    ax.plot(x_coords, y_coords, z_coords, 'k-', lw=1.5)  # Líneas negras

# Ajustar límites
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)
ax.set_box_aspect([1, 1, 1])  # Aspecto proporcional

# Títulos y etiquetas
ax.set_title("Octaedro 3D - Jenniffer", fontsize=12)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Mostrar figura
plt.show()
