#Tercer punto
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl
from skfuzzy.membership import trimf

plt.style.use('default')          # Establece el estilo por defecto de matplotlib
plt.rcParams['figure.figsize'] = (12, 8)  # Define el tamaño de figura por defecto

# Define the range of values
rango = (0, 10) # Example range, modify as needed

# Crear el universo de discurso (rango de valores posibles)
x = np.arange(rango[0], rango[1] + 1, 0.1)

# Calcular puntos clave para las funciones de membresía triangulares
min_val, max_val = rango[0], rango[1]
rango_total = max_val - min_val

# Definir puntos para funciones triangulares solapadas
# Conjunto BAJO: máximo al 0%, declina hasta 50%
bajo_points = [min_val, min_val, min_val + rango_total * 0.5]

# Conjunto MEDIO: inicia en 25%, máximo al 50%, declina hasta 75%
medio_points = [min_val + rango_total * 0.25,
                   min_val + rango_total * 0.5,
                   min_val + rango_total * 0.75]

# Conjunto ALTO: inicia en 50%, máximo al 100%
alto_points = [min_val + rango_total * 0.5, max_val, max_val]

# Generar las funciones de membresía usando skfuzzy
conjunto_bajo = fuzz.trimf(x, bajo_points)   # Función triangular para "bajo"
conjunto_medio = fuzz.trimf(x, medio_points) # Función triangular para "medio"
conjunto_alto = fuzz.trimf(x, alto_points)   # Función triangular para "alto"

# Crear la gráfica
fig, ax = plt.subplots(figsize=(10, 6))

# Graficar cada conjunto difuso
ax.plot(x, conjunto_bajo, 'b-', linewidth=2, label='Bajo')
ax.plot(x, conjunto_medio, 'g-', linewidth=2, label='Medio')
ax.plot(x, conjunto_alto, 'r-', linewidth=2, label='Alto')

# Rellenar las áreas bajo las curvas para mejor visualización
ax.fill_between(x, 0, conjunto_bajo, alpha=0.3, color='b')
ax.fill_between(x, 0, conjunto_medio, alpha=0.3, color='g')
ax.fill_between(x, 0, conjunto_alto, alpha=0.3, color='r')

# Configurar etiquetas y título
ax.set_xlabel('Valor', fontsize=12)
ax.set_ylabel('Grado de Membresía', fontsize=12)
ax.set_title('Conjuntos Difusos', fontsize=14, fontweight='bold')

# Configurar los ejes
ax.set_ylim(0, 1.1)              # Limitar eje Y entre 0 y 1.1
ax.set_xlim(rango[0], rango[1])  # Establecer límites del eje X
ax.grid(True, alpha=0.3)         # Agregar rejilla con transparencia
ax.legend(loc='upper right')     # Agregar leyenda en la esquina superior derecha

# Mejorar la apariencia
plt.tight_layout()               # Ajustar automáticamente el espaciado
plt.show()                       # Mostrar la gráfica

# EJEMPLO 1: Velocidad (0 a 100 km/h)
print("EJEMPLO 1: VELOCIDAD")
print("=" * 50)
print("Este ejemplo modela la velocidad de un vehículo usando tres conjuntos difusos:")
print("- Velocidad Baja: 0-50 km/h (máxima membresía en 0-25 km/h)")
print("- Velocidad Media: 25-75 km/h (máxima membresía en 50 km/h)")
print("- Velocidad Alta: 50-100 km/h (máxima membresía en 75-100 km/h)")


# EJEMPLO 2: Temperatura (0 a 120 °C)
print("\nEJEMPLO 2: TEMPERATURA")
print("=" * 50)
print("Modela la temperatura ambiente con tres niveles:")
print("- Temperatura Baja: 0-60°C (máxima membresía en 0-30°C)")
print("- Temperatura Media: 30-90°C (máxima membresía en 60°C)")
print("- Temperatura Alta: 60-120°C (máxima membresía en 90-120°C)")