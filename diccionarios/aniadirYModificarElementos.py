#Añadir y modificar elementos

#Creación del diccionario

contacto = {
    "nombre" : "Juan",
    "apellido" : "Perez",
    "telefono" : "123456789"
}
print(contacto)

#Modificar la clave telefono
contacto["telefono"] = "3003360232"
print(contacto["telefono"])

#Añadir una nueva clave
contacto["email"] = "julianperes@gmail.com"
print(contacto)