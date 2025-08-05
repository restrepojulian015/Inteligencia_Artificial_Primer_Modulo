#Reto: Permite que el usuario añada tareas a una lista. El programa 
# debe parar cuando el usuario escriba "terminar". 
# No permitas que se añadan tareas con menos de 4 letras.

try : 

    #Crear una lista
    lista = []

    while True :

        #Pedir la variable tarea
        tarea = input("Ingrese una tarea : ").lower()

        if tarea == 'terminar' :
            break
        elif len(tarea) < 4 :
            print("Error : La tarea debe tener al menos 4 letras")
        else :
            lista.append(tarea)
    
except Exception as error :
    print('Error : {error}')
finally :
    print("Fin del Ejercicio")