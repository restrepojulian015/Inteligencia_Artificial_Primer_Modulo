#Crea una tupla con las siguientes letras: 
# letras = ('a', 'p', 'r', 'e', 'n', 'd', 'e', 'r', ' ', 'a', ' ', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'a', 'r').
#Cuenta cuántas veces aparece la vocal "a" en la tupla.
#Imprime el resultado.

try :
    
    #Crear una tupa con las siguientes letras
    letras = ('a', 'p', 'r', 'e', 'n', 'd', 'e', 'r', ' ', 'a', ' ', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'a', 'r')
    
    for i in letras :
        if  i == 'a' :
            contador = letras.count(i)
    
    #Imprimir el resultado
    print(f'La vocal "a" aparece {contador} veces en la tupla')
except Exception as error :
    print(f'Error : {error}')
finally :
    print("Fin de la ejecución")