#usamos pandas
import pandas as pd

# Datos de los empleados
datos_empleados = {
    'ID_Empleado': ['E01', 'E02', 'E03', 'E04', 'E05', 'E06'],
    'Nombre': ['Juan', 'Ana', 'Pedro', 'Laura', 'Miguel', 'Sara'],
    'Departamento': ['Ventas', 'Marketing', 'IT', 'Ventas', 'IT', 'Marketing'],
    'Salario_Anual': [50000, 60000, 75000, 52000, 80000, 65000],
    'Antiguedad_Anios': [3, 5, 8, 2, 10, 6]
}

#Crear un DataFrame
df_empleados =  pd.DataFrame(datos_empleados)

#Imprimir el DataFrame completo
print(df_empleados)

#Muestra un resumen técnico del DataFrame para ver los tuipos de datos de cada Columna
print(df_empleados.info())

#Selecciona y muesttra únicamente las columnas 'Nombre' y 'Salario_Anual'
nombres_promedios =  df_empleados[['Nombre', 'Salario_Anual']]
print(nombres_promedios)

#Encuentra y muestra la información de todos los empleados que trabajan en el departamento IT
empleados_it = df_empleados[df_empleados['Departamento'] == 'IT']
print(empleados_it)

#Calcula y muestra el salario anual promedio de todos los empleados
salario_promedio = df_empleados['Salario_Anual'].mean()
print(salario_promedio)