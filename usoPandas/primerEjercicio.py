#Ejercicio 1 para Estudiantes: Análisis de Inventario 
#(Series)
#Has recibido los datos del inventario de una 
#tienda de electrónica en forma de una Serie de Pandas. Tu tarea es analizarla para responder a algunas preguntas.


import pandas as pd

#Datos del inventario
inventarios_productos =  {
    "Laptops" : 15,
    "Teclado" : 50,
    "Ratones" : 75,
    "Monitores" : 25,
    "Webcams" : 40,
    "Auriculares" :  30,
}

#Imprimir la serie  complerta para ver lo datos
inventario = pd.Series( inventarios_productos)
print(inventario)

#Utiliza un método para mostrar solo los ultimos 4 productos del inventario
print(inventario.tail(4))

#Encuentra y muestra los productos que tienen menos de 45 unidades en stock
productos_bajo_stock = inventario[inventario < 45]

#Calcula el número total de articulos en el inventario
total_articulos =  inventario.sum()
print(total_articulos)
