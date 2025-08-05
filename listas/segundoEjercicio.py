#Crea una lista de invitados: invitados = ["Ana", "Carlos", "David"].
#"Ana" es la anfitriona, así que debe estar al principio. Usa insert() 
# para añadir a "Elena" en la segunda posición (índice 1).
#Imprime la lista.
#Lamentablemente, "David" no puede asistir. Elimínalo de la lista usando pop() y su índice.
#Imprime la lista final de invitados.



try :
    
    #Crear lista de invitados
    invitados = ["Ana", "Carlos", "David"]
    
    print(f'Lista de invitados actual : {invitados}')
    invitados.insert(1, "Elena")
    
    #Eliminar a David de la lista
    invitados.pop(-1)
    
    #Imprimir la lista de invitados
    print(f"Lista de invitados final : {invitados}")
    
    
except Exception as error :
    print(f'Error : {error}')
finally :
    print("Fin del ejercicio")