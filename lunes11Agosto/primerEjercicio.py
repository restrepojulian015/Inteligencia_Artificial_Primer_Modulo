#Primer paso: cargar las librerias necesarias

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Segundo paso: cargar los archivos CSV

tienda1 = pd.read_csv(r"C:\Users\Usuario\Downloads\tienda_1.csv")
tienda2 = pd.read_csv(r"C:\Users\Usuario\Downloads\tienda_2.csv")
tienda3 = pd.read_csv(r"C:\Users\Usuario\Downloads\tienda_3.csv")
tienda4 = pd.read_csv(r"C:\Users\Usuario\Downloads\tienda_4.csv")

"""
Cada DataFrame contiene todas las columnas: 
propucto, Categoría, Precio, etc.
"""

#Tercer paso: Agregar identificadores
tienda1['Tienda'] = 'Tienda 1'
tienda2['Tienda'] = 'Tienda 2'
tienda3['Tienda'] = 'Tienda 3'
tienda4['Tienda'] = 'Tienda 4'

"""
Qué hace cada linea?

Agrega una nueva columna llamada 'Tienda_x' a cada DataFrame
Esta columna identifica de qué tieenda proviene cada registro.
Es crucial para poder diferenciar las tiendas cuando combinemos los datos.
"""

#Cuarto paso: Conmcatenar los datos

#Este paso combina los DataFrames de las cuatro series de las tiendas en uno solo

tienda_completa = pd.concat([tienda1,tienda2, tienda3, tienda4], ignore_index = True)

print("Datos combinados de todos los datos:")
print("\n", tienda_completa.head())

#Quinto paso: Informacion general
print("\nInfdormación general del dataset:")
print(f"Total de registro: {len(tienda_completa)}")
print(f"Registros por tienda:")
print(tienda_completa['Tienda'].value_counts())
print("\n" + "=" * 50)

#sexta paso: análisis de facturación
facturacion_por_tienda = tienda_completa.groupby('Tienda')['Precio'].agg(['sum','count','mean']).round(2)


#Renombrar las columnas para mayor claridad
facturacion_por_tienda.columns = ['Facturación_Total', 'Cantidad_Ventas',
'Precio_Promedio']

#Odenar las tiendas de mayor a menor facturación
facturacion_por_tienda = facturacion_por_tienda.sort_values('Facturación_Total', ascending=False)

print("\Facturación por tienda:")
print(facturacion_por_tienda)


#Séptimo paso: Visualización de datos

# plt.figure(figsize=(12, 8))

# #Crea una figura de 12*8 pulgadas para los gráficos


# plt.subplot(2,2,1)

# #Crea una grilla de 2*2 subgráficos y selecciona el primero

# facturacion_por_tienda['Facturación_Total'].plot(kind='bar', color='skyblue')

# """ 
# * Crea un gráfica der barras de la facturación total
# * Kind =m 'bar Tipo de Gráfico de barras
# * Color = 'skyblue color de las barras
# """

# plt.title('Facturación Total por Tienda')
# plt.ylabel('Factuación Total')
# plt.xticks(rotation=45)

# plt.show()

#análisis de 

# productos_mas_vendidos = tienda_completa['Producto'].value_counts().head(5).index

# df_top_productos = tienda_completa[tienda_completa['Producto'].isin(productos_mas_vendidos)]



# productos_por_tienda = df_top_productos.groupby('Producto')['Precio'].agg(['count','sum','mean']).round(2)

# productos_por_tienda.columns = ['Cantidad_Vendida', 'Facturación_Total','Precio_Promedio']

# #Imrpimirv los el Nuevo DataFrame
# print(productos_por_tienda.head())

# #Visualización de los productos más vendidos

# plt.figure(figsize=(12,8))

# plt.subplot(2,2,1)

# productos_por_tienda['Cantidad_Vendida'].plot(kind='bar', color='lightgreen')
# plt.title('Productos más Vendidos')
# plt.ylabel('Cantidad Vendida')
# plt.xticks(rotation=45)

# plt.show()


#Análisis por categorías
ventas_categorias = tienda_completa.groupby(['Tienda','Categoría del Producto'])['Precio'].agg(['sum','count']).round(2)


print(ventas_categorias)
"""
Qué hace esta linea?

*  groupby(['tienda','Categoria del Producto']): Agrupa por dos criterios
* Calcula suma y conteo de precios para calcular cada combinación tienda-categoria
"""

categoria_total = tienda_completa.groupby('Categoría del Producto')['Precio'].sum().sort_values(ascending = False)

"""
* Calcula facturación total por categoría (sin importar la tienda)
* Ordena de mayor a menor
"""

print(categoria_total)

#Sección 11: Pivot Table

pivot_categoria = tienda_completa.pivot_table(values = 'Precio', index='Categoría del Producto', columns = 'Tienda', aggfunc='sum', fill_value=0)

print(pivot_categoria)

"""
pivot_table(): Crea una tabla dinámica
values='Precio': Los valores a sumar
index='Categora del Producto': Filas de la tabla
aggfunc = 'sum': Función de agregación (suma)
fill_value = 0: Rellena valores faltantes con 0
"""

#Sección 12: Análisis de calficaciones

calificacion_tienda = tienda_completa.groupby('Tienda')['Calificación'].agg(['mean', 'count','std']).round(2)

print(calificacion_tienda)

#Sección 13: Análisis de productos

productos_cantidad = tienda_completa.groupby('Producto').agg({
'Precio': ['count', 'sum', 'mean']
}).round(2)

"""
¿Qué hace esta línea?
• Agrupa por producto
• Para cada producto calcula:
    o count: Cuántas veces se vendió
    o sum: Facturación total del producto
    o mean: Precio promedio del producto
"""

productos_cantidad.columns = ['Cantidad_Vendida', 'Facturación_Total',
'Precio_Promedio']

#Seccion 14 : Productos Top por tienda
productos_por_tienda = tienda_completa.groupby(['Tienda',
'Producto']).size().reset_index(name='Cantidad')

"""
• Cuenta cuántas veces se vendió cada producto en cada tienda
• .size(): Cuenta registros
• .reset_index(name='Cantidad'): Convierte el resultado en DataFrame con
columna 'Cantidad'
"""