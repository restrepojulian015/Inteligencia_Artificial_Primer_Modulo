import pandas as pd

#Creación de una Data
datos_estudiantes = {
    'Nombre': ['Julian','Luis','Carlos','Marta','sofia'],
    'Edad': [20, 22, 21, 23, 22],
    'Carrera': ['Economía', 'Ingeniería', 'Economía', 'Derecho', 'Ingeniería'],
    'Semestre': [4, 6, 5, 8, 7],
    'Promedio': [8.5, 9.1, 7.8, 8.9, 9.3]

}

#Creación del DataFrame
data_estudiantes =  pd.DataFrame(datos_estudiantes)

#Imprimir el DataFrame para verlo
print(data_estudiantes)

# Usar .describe()
print(data_estudiantes.describe())

#seleccionar solo la columna 'Nombre' y 'Promedio'
nombres_promedios = data_estudiantes[['Semestre', 'Promedio']]
print(nombres_promedios)

#Uso de .loc y .iloc
print(data_estudiantes.loc[2])

#Uso de .iloc
print(data_estudiantes.iloc[1])