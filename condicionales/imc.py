# Pide al usuario en kg y su altura en metros. Calcule el IMC (peso / (altura)^2). Clasifícalo: Menor a 18.5 "Bajo peso",
#18.5-24.9 "Normal", 25-29.9 "Sobrepeso", 30 o mayor "Obesidad".

try :
    #Recibe la variable altura
    altura = float(input('Ingrese la altura en Metros: '))
    #Pide la variable peso
    peso = float(input('Ingrese el peso en Kilogramos: '))

    imc = peso / (altura ** 2)


    #Condicional
    if imc < 18.5 :
        print('Bajo Peso')
    elif 18.5 <= imc <= 24.5 :
        print('Normal')
    elif 25 <= imc <= 29.9 :
        print('SobrePeso')
    elif imc >= 30 :
        print('Obesidad')
    else :
        print('IMC no valido')
except ValueError as error :
    print(f'Error: {error}')
except Exception as error :
    print(f'Error inesperado: {error}')
finally :
    print('Fin del ejercico')