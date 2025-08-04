# Reto: Crea un menú que se repita hasta que el usuario elija la opción "3. Salir"
# .Las opciones son: "1. Saludar", "2. Contar un chiste", "3. Salir".
#Pista: Usa un bucle while. Dentro del bucle, pide la opción y usa if/elif/else para mostrar 
# el mensaje correspondiente a cada opción. La condición del while debe ser que la opción sea diferente de "3".

from gettext import find


try : 

    while True :
        print("=======Menú=======")
        print("1. Saludar")
        print("2. Contar un chiste")
        print("3. Salir")
        print("==================")

        #Pedir la variable opcion
        opcion = int(input("Ingrese su opción: "))

        #Condicional
        if opcion == 3 :
            break
        elif opcion == 1 : 
            print("Hola")
        elif opcion == 2 :
            print("Porque los peces no usan Facebook? Porque le tienen miedo a la red.")
        else :
            print("Opción no valida")

except ValueError as error :
    print(f'Error : {error}')
except Exception as error :
    print(f'Error inesperado : {error}')
finally :
    print("Fin del Ejercicio")
