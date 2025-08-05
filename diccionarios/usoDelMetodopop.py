#Uso del Método pop() para eliminar un elemento

#Creación del dicccionario
tareas_pendientes = {
    "lunes"  : "Reunión",
    "Martes" : "Entregar reporte",
    "Miercoles" : "Llamar Cliente"
}

#Uso de pop()
tarea = tareas_pendientes.pop("lunes")
print(tarea)
print(tareas_pendientes)