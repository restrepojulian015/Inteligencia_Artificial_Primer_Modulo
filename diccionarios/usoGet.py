#Uso del Método get() para obtener un valor de una llave de un diccionario
#Si no lo encuentra devulve None en vez de arrojar un error

#Creación del diccionario
coche = {"marca" : "Ford", "modelo" : "Mustang"}

#obtener un valor que existe
marca = coche.get("marca")
print(marca)

#Obtener un valor que no existe
noExistente = coche.get("Año")
print(noExistente)