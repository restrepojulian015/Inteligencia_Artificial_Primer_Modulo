#Reto: Crea un programa que pida 6 veces una palabra. Por cada palabra, 
# indica si empieza con una vocal o con una consonante.

try :
    for i in range(6) :
        #Pedir la variable palabra
        palabra = input("Ingrese una palabra : ").lower()
        if palabra[0] in 'aeiou' :
            print("Empieza con una vocal")
        else :
            print("Empieza con una consonante")
except Exception as error :
    print(f'Error : {error}')
finally :
    print("Fin del Ejercicio")