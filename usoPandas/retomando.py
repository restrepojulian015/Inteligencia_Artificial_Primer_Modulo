#Primer paso, importar la librería pandas
import pandas as pd

#Segtundo paso, cargar el archivo CSV
df_archivo =  pd.read_csv(r"C:\Users\Usuario\AppData\Local\Temp\1bdd895f-57dd-4d59-b8f0-8012f22362b9_archive.zip.2b9\train_and_test2.csv")


#Tercer paso. imprimir las 5 filas
print("Imprimir las primeras  5 filas:")
print(df_archivo.head())

#Cuarto paso, obtenber la información del DataFrame
print("Infomrmaación General del DataFrame:")
print(df_archivo.info())

#quinto paso, obtener estadística descriptiva de las columnas númericas
print("\nEstadística Descriptiva del archivo df_archivo:")
print(df_archivo.describe())

"""
.head(): Muestra las primeras n filas (por defecto 5).
.tail(): Muestra las últimas n filas (por decto 5).
.info(): Proporciona un resumen consiso del DataFrame, 
incluido el tipo de datos de cada columna y si hay valores nulos-
.describe() : Genera estadísticas descriptivas para las columnas 
numéricas, como el recuento, la media, la desviación estándar, 
los valores minimos y máximmos, y los percentiles.
"""
