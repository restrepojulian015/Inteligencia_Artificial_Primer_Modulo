#Enunciado:
#Tienes una lista de puntuaciones de un torneo: puntuaciones = [88, 95, 72, 100, 85].
#Ordena las puntuaciones de menor a mayor e imprime la lista.
#Ahora, ordena las puntuaciones de mayor a menor (la clasificación real) e imprime la lista.

try :
    
    #Crear lista de puntuaciones
    puntuaciones = [88, 95, 72, 100, 85]
    
    #Ordenar de menor a mayor
    puntuaciones.sort( reverse = False)
    
    print(puntuaciones)
    
    puntuaciones.sort( reverse = True)
    
    print(puntuaciones)
    
except Exception as error :
    print(f'Error : {error}')
finally :
    print("Fin del ejercicio")