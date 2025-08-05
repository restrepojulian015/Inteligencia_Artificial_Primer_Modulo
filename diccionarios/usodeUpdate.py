#Uso del método update()

#Creaación de diccionarios

perfil_usuario = {
    "nombre" : "Juan",
    "ciudad" : "Madrid"
}

datos_adicionales = {
    "ciudad" : "Barcelona",
    "profesion" : "Desarrollador"
}

print(perfil_usuario)
print(datos_adicionales)

#Actualizar perfil_usuario
perfil_usuario.update(datos_adicionales)

#Imprimir actualización
print(perfil_usuario)