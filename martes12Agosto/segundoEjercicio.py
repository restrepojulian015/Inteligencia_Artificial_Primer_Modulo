#Segundo Ejercicio.py
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl
from skfuzzy.membership import trimf


rango = (0,10)
x = np.arange(rango[0], rango[1] + 1, 0.1)


min_val = rango[0] 
max_val = rango[1]
rango_total = max_val - min_val
#Calculamos las membresia
bajo_points = [min_val, min_val, min_val + rango_total * 0.5]


conjunto_bajo = fuzz.trimf(x, bajo_points)
colores = ('blue','orage','greem')

nombres_conjuntos = ('bajo','medio','alto')

figure, ax = plt.subplots(figsize = (8,5) )
ax.plot(x, conjunto_bajo, colores[0], linewidth=2, label=nombres_conjuntos[0])
ax.fill_between(x, 0, conjunto_bajo, alpha=0.3, color=colores[0][0])

plt.show()
