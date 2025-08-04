#Reto: Pide un número del 10 al 20. Haz una cuenta regresiva desde ese número hasta 1. 
# Cuando la cuenta llegue a 5, imprime el mensaje "¡Casi llegamos!".
#Pista: Usa un bucle for con range para contar hacia atrás (ej: range(numero, 0, -1)). Dentro, un if verificará si el número actual es 5.

try :

    while True :
        #Pedir la variable número
        numero = int(input("Ingrese un Número del 10 al 20 :  "))
        if numero < 10 or numero > 20 :
            print("Error : El número debe estar en le rango 10 a 20")
        else :
            for i in range(numero, 0, -1) :
                if i == 5 :
                    print("¡Casi llegamos!")
                print(i)
            break
        
except ValueError as error :
    print(f'Error : {error}')
except Exception as error :
    print(f'Error inesperado : {error}')
finally :
    print("Fin del Ejercicio")