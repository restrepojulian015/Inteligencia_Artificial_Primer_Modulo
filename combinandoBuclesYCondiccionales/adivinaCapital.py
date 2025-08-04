#Reto: Establece una capital secreta (ej: "Bogota"). Dale al usuario 3 intentos para adivinarla. Si acierta, felicítalo y termina el juego. Si falla, dile "Incorrecto, intenta de nuevo". Si se le acaban los intentos, dile cuál era la respuesta correcta.
#Pista: Usa un bucle for con range(3). Dentro, pide la respuesta y con un if compárala con la capital secreta. Puedes usar break si el usuario acierta.

try : 
    #Establecer la capital secreta
    capitalSecreta = "BOGOTÁ"

    #Ciclo
    for i in range(3) :
        
        #Pedir la variable capital
        capital = input("Ingrese la capital: ").upper()

        #Condicional
        if capital == capitalSecreta :
            print("Correcto")
            break
        else :
            print(f'Incorrecto, intento : {i + 1}')
except Exception as error :
    print(f'Error : {error}')
finally :
    print('Fin del Ejercicio')