import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Coordenadas 3D de los vértices de un dodecaedro
phi = (1 + np.sqrt(5)) / 2  # Número áureo

puntos = {
    "P1": (-1, -1, -1),
    "P2": (-1, -1,  1),
    "P3": (-1,  1, -1),
    "P4": (-1,  1,  1),
    "P5": ( 1, -1, -1),
    "P6": ( 1, -1,  1),
    "P7": ( 1,  1, -1),
    "P8": ( 1,  1,  1),
    "P9": ( 0, -phi, -1/phi),
    "P10": ( 0, -phi,  1/phi),
    "P11": ( 0,  phi, -1/phi),
    "P12": ( 0,  phi,  1/phi),
    "P13": (-phi, -1/phi, 0),
    "P14": (-phi,  1/phi, 0),
    "P15": ( phi, -1/phi, 0),
    "P16": ( phi,  1/phi, 0),
    "P17": (-1/phi, 0, -phi),
    "P18": (-1/phi, 0,  phi),
    "P19": ( 1/phi, 0, -phi),
    "P20": ( 1/phi, 0,  phi)
}

# Conexiones entre los puntos para formar las caras del dodecaedro
conexiones = [
    ("P1", "P3"), ("P1", "P5"), ("P1", "P9"), ("P1", "P13"), ("P1", "P17"),
    ("P2", "P4"), ("P2", "P6"), ("P2", "P10"), ("P2", "P14"), ("P2", "P18"),
    ("P3", "P7"), ("P3", "P11"), ("P3", "P13"),
    ("P4", "P8"), ("P4", "P12"), ("P4", "P14"),
    ("P5", "P7"), ("P5", "P15"), ("P5", "P19"),
    ("P6", "P8"), ("P6", "P15"), ("P6", "P20"),
    ("P7", "P11"), ("P7", "P16"), ("P7", "P19"),
    ("P8", "P12"), ("P8", "P16"), ("P8", "P20"),
    ("P9", "P10"), ("P9", "P13"), ("P9", "P15"),
    ("P10", "P14"), ("P10", "P18"), ("P10", "P20"),
    ("P11", "P12"), ("P11", "P16"), ("P11", "P17"),
    ("P12", "P14"), ("P12", "P18"),
    ("P13", "P17"), ("P14", "P18"),
    ("P15", "P19"), ("P16", "P20")
]

# Crear figura 3D
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Graficar puntos
for nombre, coord in puntos.items():
    ax.scatter(*coord, label=nombre, s=50)  # Dibujar puntos
    ax.text(coord[0] + 0.1, coord[1] + 0.1, coord[2], nombre, fontsize=8)  # Etiquetas

# Dibujar conexiones
for p1, p2 in conexiones:
    x_coords = [puntos[p1][0], puntos[p2][0]]
    y_coords = [puntos[p1][1], puntos[p2][1]]
    z_coords = [puntos[p1][2], puntos[p2][2]]
    ax.plot(x_coords, y_coords, z_coords, 'k-', lw=1.5)  # Líneas negras

# Ajustar límites
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)
ax.set_box_aspect([1, 1, 1])  # Aspecto proporcional

# Títulos y etiquetas
ax.set_title("Dodecaedro 3D - Jenniffer", fontsize=12)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Mostrar figura
plt.show()
