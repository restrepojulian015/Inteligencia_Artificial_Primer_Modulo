#Uso del método popItem()

#Creación del diccionario
inventario = {
    "manzana" : 100,
    "bananas" : 150,
    "naranjas" : 120
}

print(inventario)

#Uso del método popItem()

item = inventario.popitem()
print(item)
print(inventario)