#Pide un total de compra. Si es mayor a  $100.000, aplica un 10% de descuento. Si no, no hay descuento. Muestra el total a pagar

try:
    #Pedir el valor
    valor = int(input("Ingrese el total de la compra: "))

    #Condicional
    if valor > 100000 :
        descuento = valor*0.1
        print(f'Descuento: {descuento}\nTotal a pagar: {valor-descuento}')
    else : 
        print(f'No hay descuento\nTotal a pagar: {valor}')

except ValueError as error:
    print(f'Error: {error}')
except Exception as e :
    print(f'Error inesperado: {e}')
finally:
    print("Fin del Ejercicio")