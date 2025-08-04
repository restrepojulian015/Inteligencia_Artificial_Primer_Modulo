#Reto: Muestra todos los números del 1 al 50. Si un número es múltiplo de 3, 
# mprime " (Múltiplo de 3)" al lado. Si es múltiplo de 5, imprime " (Múltiplo de 5)". Si es múltiplo de ambos, debe mostrar ambos mensajes.


try : 

    for i in range(1,51) :
        if i % 3 == 0 and i % 5 == 0 :
            print(f'{i} es multiplo de 3 y de 5\n')
        elif i % 3 == 0 :
            print(f'{i} es multiplo de 3\n')
        elif i % 5 == 0 :
            print(f'{i} es multiplo de 5\n')
        else :
            print('No es multiplo de 3 ni de 5\n')
except ValueError as error : 
    print(f'Error : {error}')
except Exception as error :
    print(f'Error {error}')
finally :
    print("Fin de la operación")