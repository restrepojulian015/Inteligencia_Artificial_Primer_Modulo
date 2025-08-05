#Planificador de Itinerarios de Viaje

#Crearemos un itinerario que guarda ciudades a visitar, y para cada ciudad, una lista de actividades con su costo y duración.
#Estructura de Datos:
#Un diccionario para el itinerario, donde la clave es el nombre de la ciudad.
#El valor para cada ciudad es otro diccionario con datos como 'país'.
#Dentro del diccionario de la ciudad, una clave 'actividades' contendrá una lista.
#Cada actividad en la lista será una tupla (nombre_actividad, duracion_horas, costo_usd).

try :
    
    #Estructura de Datos
    itinerario_viaje = {
        "París": {
            "país": "Francia",
            "actividades": [
                ("Visita a la Torre Eiffel", 3, 30.0),
                ("Recorrido por el Museo del Louvre", 5, 25.0),
                ("Paseo por Montmartre", 4, 0.0)
            ]
        },
        "Roma": {
            "país": "Italia",
            "actividades": [
                ("Visita al Coliseo", 3, 22.5),
                ("Explorar el Vaticano", 6, 20.0),
                ("Comer Gelato en Trastevere", 1, 5.0)
            ]
        }
    }
    print("Itinerario inicial creado.")
    
        # --- Calcular costo total en París ---
    ciudad = "París"
    costo_total = 0

    # 1. Acceder al diccionario de la ciudad
    if ciudad in itinerario_viaje:
        # 2. Obtener la lista de actividades (que son tuplas)
        lista_actividades = itinerario_viaje[ciudad]["actividades"]

        # 3. Sumar el costo de cada actividad
        for _, _, costo in lista_actividades: # Usamos _ para ignorar nombre y duración
            costo_total += costo

        print(f"\nEl costo total de las actividades en {ciudad} es: ${costo_total:.2f} USD")
    else:
        print(f"La ciudad {ciudad} no está en el itinerario.")
        
    # --- Encontrar actividades largas ---
    print("\nBuscando actividades de larga duración (>4 horas)...")

    # 1. Iterar sobre cada ciudad y sus detalles en el itinerario
    for ciudad, detalles_ciudad in itinerario_viaje.items():
    # 2. Obtener la lista de actividades para la ciudad actual
        actividades = detalles_ciudad["actividades"]

        # 3. Iterar sobre cada tupla de actividad
        for nombre_act, duracion, _ in actividades:
            # 4. Comprobar si la duración cumple la condición
            if duracion > 4:
                print(f"- En {ciudad}: {nombre_act} (Duración: {duracion} horas)")


except ValueError as error :
    print(f'Error : {error}')
finally :
    print('Fin de la Ejecución')