#Pide una nota del 0 al 10. Muestra "Repobado" si es menor de 5,
# Aprobado" si está entre 5 y  8, "sobresaliente" si es mayor a 8  y menor o igual a 10.

try :
    #Pedir la variable nota
    nota = int(input("Ingrese su nota del 0 al 10: "))

    #Condicional
    if nota < 5 :
        print("Reprobado")
    elif 5 <= nota < 8 :
        print('Aprobado')
    elif 8 <= nota <= 10 :
        print('Sobresaliente')
    else :
        print("Nota no valida")
except Exception as error :
    print(f'Error : {error}')
finally : 
    print("Fin de la prueba.")