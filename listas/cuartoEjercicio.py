#Crea dos listas de equipos: equipo_azul = ["Sara", "Miguel"] y equipo_rojo = ["Lucía", "Juan"].
#El equipo_azul ha ganado y absorberá a los miembros del equipo_rojo. Usa extend() para añadir los miembros del equipo rojo al azul.
#Imprime la lista final del equipo_azul.

try :
    
    #Crear  dos listas de equipos
    equipo_azul = ["Sara", "Miguel"]
    
    equipo_rojo = ["Lucía", "Juan"]

    #Añadir los miembros del equipo rojo al azul
    equipo_azul.extend(equipo_rojo)
    
    print(f'Equipo Azul final : {equipo_azul}')    
except Exception as error :
    print(f'Error : {error}')
finally :
    print("Fin de la ejecución")