#Un punto en un mapa 2D se representa con una tupla, por ejemplo: punto_origen = (0, 0).
#Intenta cambiar el primer elemento de la tupla a 10 para "mover" el punto.
#Observa el error que Python genera y explica por qué sucede.

try :

    # Crear un punto en un maapa 2D
    punto_origen = (0,0)
    
    # No se puede mover

except TypeError as error:
    print(f'Error: {error}')