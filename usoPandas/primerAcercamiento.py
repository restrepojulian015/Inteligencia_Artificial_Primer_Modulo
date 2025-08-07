import pandas as pd

#Datos de ejemplo

datos_frutas = [30,45,25,50,22]
indice_frutas = ['Manzana','Naranja','Bananas','Fresas','Kiwis']

#Creación de la Serie
ventas_frutas = pd.Series(datos_frutas, index = indice_frutas, name = 'Ventas de Dia')

#Imprimir la Serie para verla
print(ventas_frutas)

"""
Usar .head() y tail() se usan para podeer mostrar los primeros y l  os últimos.
"""
print(ventas_frutas.head())
print(ventas_frutas.tail())
print(ventas_frutas.describe())