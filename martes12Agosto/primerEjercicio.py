import numpy as np
import skfuzzy as fuzz

from skfuzzy import control as ctrl

# 1. IMPORTAR HERRAMIENTAS
import numpy as np
import skfuzzy as fuzz

from skfuzzy import control as ctrl

# 2. DEFINIR LAS VARIABLES
# Velocidad de entrada (0 a 100 km/h)
velocidad = ctrl.Antecedent(np.arange(0, 101, 1), 'velocidad')
# Fuerza de salida (0 a 100%)
fuerza = ctrl.Consequent(np.arange(0, 101, 1), 'fuerza')

# 3. CREAR LOS CONJUNTOS DIFUSOS
# Para velocidad
velocidad['baja'] = fuzz.trimf(velocidad.universe, [0, 0, 50])
velocidad['media'] = fuzz.trimf(velocidad.universe, [25, 50, 75])
velocidad['alta'] = fuzz.trimf(velocidad.universe, [50, 100, 100])

# Para fuerza
fuerza['menos'] = fuzz.trimf(fuerza.universe, [0, 0, 50])
fuerza['normal'] = fuzz.trimf(fuerza.universe, [25, 50, 75])
fuerza['más'] = fuzz.trimf(fuerza.universe, [50, 100, 100])

# 4. CREAR LAS REGLAS
regla1 = ctrl.Rule(velocidad['alta'], fuerza['menos'])
regla2 = ctrl.Rule(velocidad['media'], fuerza['normal'])
regla3 = ctrl.Rule(velocidad['baja'], fuerza['más'])

# 5. CREAR EL SISTEMA Y SIMULAR
sistema = ctrl.ControlSystem([regla1, regla2, regla3])

simulacion = ctrl.ControlSystemSimulation(sistema)

# 6. PROBAR CON UN VALOR
simulacion.input['velocidad'] = 60
simulacion.compute()

print(f"Para 60 km/h, fuerza sugerida: {simulacion.output['fuerza']:.1f}%")