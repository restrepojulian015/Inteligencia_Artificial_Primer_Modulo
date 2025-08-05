#Objetivo: Usar copy() y modificar la copia.
#Enunciado:
#Crea una lista base de cosas para llevar a un viaje: viaje_base = ["pasaporte", "dinero", "cargador"].
#Estás planeando dos viajes: uno a la playa y otro a la montaña. Crea dos copias de la lista base, llamadas viaje_playa y viaje_montana.
#Al viaje_playa añádele "toalla" y "bañador".
#Al viaje_montana añádele "botas" y "abrigo".
#Imprime las tres listas para ver que la original no cambió y las copias son diferentes.

try :
    
    #Crear una lista de cosas para llevar a  un viaje
    viaje_base = ["pasaporte", "dinero", "cargador"]
    
    #crear dos copias
    viaje_playa = viaje_base.copy()
    viaje_montana = viaje_base.copy()
    
    #Añadir a playa toalla y bañador
    viaje_playa.append("toalla")
    viaje_playa.append("bañador")
    
    #Añadir a montaña botas y abrigo
    viaje_montana.append("botas")
    viaje_montana.append("abrigo")
    
    print(f'Viaje a la playa: {viaje_playa}')
    print(f'Viaje a la montaña: {viaje_montana}')
    print(f'Viaje base: {viaje_base}')
    
except  Exception as error :
    print(f'Error : {error}')
finally :
    print("Fin de la operación")