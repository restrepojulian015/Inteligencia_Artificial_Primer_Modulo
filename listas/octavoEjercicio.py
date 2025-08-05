#Objetivo: Usar clear().
#Enunciado:
#Crea una lista de tareas pendientes: tareas = ["Lavar ropa", "Comprar víveres", "Pasear al perro"].
#Imprime la lista de tareas.
#¡Felicidades, has completado todas tus tareas! Vacía la lista para reflejar que no tienes nada pendiente.
#Imprime la lista vacía.

try :
    
    #Crear  una lista de tareas pendientes
    tareas = ["Lavar ropa", "Comprar víveres", "Pasear al perro"]
    
    #Imprimir la lista de tareas
    print(f'La lista de tareas pendientes es : {tareas}')
    
    tareas.clear()
    
    print(tareas)
except Exception as error :
    print(f'Error : {error}')
finally :
    print(f'Fin del Ejercicio')