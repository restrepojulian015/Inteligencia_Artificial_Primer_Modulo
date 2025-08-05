#Tienes una tupla con los nombres de los finalistas en el orden en que terminaron una carrera: finalistas = ("Mario", "Luigi", "Yoshi", "Bowser").
#Necesitas encontrar la posición (índice) de "Yoshi".
#Imprime un mensaje que diga en qué posición terminó "Yoshi" (recuerda que los índices empiezan en 0).

try :
    
    #crear una tupla con  los nombres de los finalistas
    finalistas = ("Mario", "Luigi", "Yoshi", "Bowser")
    
    #Encontrar la posición (índice) de Yoshi
    posicion = finalistas.index("Yoshi") + 1
    
    #Imprimir un mensaje que diga en qué posición terminó Yoshi
    print(f'Yoshi terminó en la posición (índice) : {posicion}')
except Exception as error :
    print(f'Error : {error}')
finally :
    print("Fin de la ejecución")