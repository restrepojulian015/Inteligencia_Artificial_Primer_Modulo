#Reto: Permite que el usuario añada tareas a una lista. El programa debe parar cuando el 
# usuario escriba "terminar". No permitas que se añadan tareas con menos de 4 letras.

try :

    list = []

    while True:

        #Añadir un tarea
        tarea = input("Ingresa una tarea: ").lower()
        if tarea == 'terminar' :
            break
        list.append(tarea)

except Exception as error :
    print(f'Error: {error}')
finally :
    print('fin de la Ejecución.')