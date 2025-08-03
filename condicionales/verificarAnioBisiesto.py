#Pide un año y determina si es bisiesto. Un año es bisiesto si es divisible por 4, 
# excepto si es divisible por 100 pero no por 400.

try:
    #Pedir el año
    anio = int(input("Ingrese el Año: "))

    #Condicional
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0) :
        print("Bisiesto.")
    elif len(str(anio)) != 4 :
        print("Ingrese un año valido.")
    else :
        print("No es Bisiesto.")
except ValueError as error:
    print(f'Erro: {error}')
except Exception as error :
    print(f'Error inesperado: {error}')
finally:
    print("Fin del Ejercicio")