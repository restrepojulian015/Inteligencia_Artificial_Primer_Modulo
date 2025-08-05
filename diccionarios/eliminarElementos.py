#Eliminar elementos

#Creación del diccionario
configuracion = {
    "usuario" : "admin",
    "tema" : "oscuro",
    "version" : "1.5"
}

print(configuracion)

#Eliminar la clave usuario
del configuracion["tema"]

#Imprimir el diccionario
print(configuracion)