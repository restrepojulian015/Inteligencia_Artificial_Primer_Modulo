#Pide el tipo de vehículo ("carro" o "moto"). Pide el número de horas. La tarifa para carros es $4.000/hora, 
# para motos es $2.000/hora. Calcula y muestra el total a pagar.

#Imprimir el menu
print("=======Menú=======")
print("1. Carro")
print("2. Moto")
print("==================")

try :
    #Pedir la variable horas
    horas = int(input("Ingrese el número de Horas: "))
    #Pedir la variable tipo de Tickete
    tipoTickete = int(input("Ingrese el tipo de tickete (carro o moto): "))

    #Condicional
    if tipoTickete == 1 :

        total = horas * 4000
        print(f'Total a pagar : {total} Pesos')
    elif tipoTickete == 2 :
        total = horas * 2000
        print(f'Total a pagar : {total} Pesos')
    else :
        print("Tipo de tickete no valido")        
except Exception as error :
    print(f'Error: {error}')
finally :
    print("Fin del Ejercicio")