import sys
from App import logic as l


default_limit = 1000
sys.setrecursionlimit(default_limit*10)

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    catalog = l.new_logic()
    return catalog

    pass

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    filename = input("Ingrese el nombre del archivo: ")
    _,tiempo,total,menor_dist,mayor_dist,primeros,ultimos = l.load_data(control, filename)
    return _,tiempo,total,menor_dist,mayor_dist,primeros,ultimos

    pass


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    id = input("Ingrese el indice del dato a consultar: ")
    print(l.get_data(control, id))
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    try:
        p = int(input("Cantidad de pasajeros a filtrar (1,2,3,5...): ").strip())
    except:
        print("Valor inválido.")
        return
    res = l.req_1(control, p)
    print("\n--- Resultado Requerimiento 1 ---")
    print(f"Tiempo de ejecución (ms): {res['tiempo_ms']}")
    print(f"Número total de trayectos: {res['total_trayectos']}")
    print(f"Tiempo promedio (min): {res['prom_duracion_min']}")
    print(f"Costo total promedio (USD): {res['prom_costo_total']}")
    print(f"Distancia promedio (millas): {res['prom_dist_millas']}")
    print(f"Peajes promedio (USD): {res['prom_peajes']}")
    print(f"Tipo de pago más usado: {res['pago_mas_usado']}")
    print(f"Propina promedio (USD): {res['propina_promedio']}")
    print(f"Fecha de inicio más frecuente: {res['fecha_mas_frecuente']}")
    print("---------------------------------\n")
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    m_pago = str(input("Ingrese el metodo de pago a filtrar: "))
    res =l.req_2(control, m_pago)
    print("\n--- Resultado Requerimiento 2 ---")
    print(f"Tiempo de ejecución (ms): {res['Tiempo de ejecucion (ms)']}")
    print(f"Número total de trayectos: {res['Trayectos totales']}")
    print(f"Trayectos filtrados: {res['Trayectos filtrados']}")
    print(f"Duracion promedio por trayecto (min): {res['Duracion promedio p/trayecto (min)']}")
    print(f"Costo promedio(USD): {res['Coste promedio (USD)']}")
    print(f"Distancia promedio (millas): {res['Distancia promedio (millas)']}")
    print(f"Costo promedio de peajes (USD): {res['Coste de peaje promedio']}")
    print(f"Propina promedio (USD): {res['Propina promedio']}")
    print(f"# de pasajeros mas frecuente: {res["Pasajero mas frecuente"]}")
    print(f"Fecha de finalizacion más frecuente: {res['Frecuencia de fecha']}")
    print("---------------------------------\n")
    

def print_req_3(control):
    pago_min = float(input("Ingrese el pago mínimo: "))
    pago_max = float(input("Ingrese el pago máximo: "))
    res = l.req_3(control, pago_min, pago_max)
    print("\n--- Resultado Requerimiento 3 ---")
    print(f"Tiempo de ejecución (ms): {res['tiempo de ejecucion (ms)']}")
    print(f"Trayectos que cumplen el rango: {res['total de viajes válidos']}")
    print(f"Duracion promedio por trayecto (min): {res['promedio duración (min)']}")
    print(f"Costo promedio(USD): {res['promedio costo (USD)']}")
    print(f"Distancia promedio (millas): {res['promedio distancia (millas)']}")
    print(f"Costo promedio de peajes (USD): {res['promedio pago peajes']}")
    print(f"# de pasajeros mas frecuente: {res["num pasajeros mas frecuente"]}")
    print(f"Propina promedio (USD): {res['promedio propinas']}")
    print(f"Fecha de finalizacion más frecuente: {res['fecha final mas frecuente']}")
    print("---------------------------------\n")

def print_req_4(control):
    
    f_costo = input("Ingrese el filtro de costo: ")
    if f_costo != "MAYOR" and f_costo != "MENOR":
        print("El filtro de costo debe ser \"MAYOR\" o \"MENOR\"")
        f_costo = input("Ingrese nuevamente el filtro de costo: ")

    f_inicial = input("Ingrese la fecha inicial (AAAA-MM-DD): ")
    f_final = input("Ingrese la fecha final (AAAA-MM-DD): ")
    res =l.req_4(control, f_costo, f_inicial, f_final)
    print("\n--- Resultado Requerimiento 4 ---")
    print(f"Tiempo de ejecución (ms): {res['tiempo de ejecucion (ms)']}")
    print(f"Filtro seleccionado del costo: {res['filtro']}")
    print(f"Trayectos que cumplen el filtro: {res['total de viajes filtrados']}")
    print(f"Barrio de origen: {res["barrio de origen"]}")
    print(f"Barrio de destino: {res["barrio de destino"]}")
    print(f"Distancia promedio (km): {res['distancia promedio (km)']}")
    print(f"Duracion promedio por trayecto (min): {res['duracion promedio (min)']}")
    print(f"Costo total promedio(USD): {res['costo promedio (USD)']}")
    print("---------------------------------\n")

def print_req_5(control):
    
    f_costo = input("Ingrese el filtro de costo: ")
    if f_costo != "MAYOR" and f_costo != "MENOR":
        print("El filtro de costo debe ser \"MAYOR\" o \"MENOR\"")
        f_costo = input("Ingrese nuevamente el filtro de costo: ")

    f_inicial = input("Ingrese la fecha inicial (AAAA-MM-DD): ")
    f_final = input("Ingrese la fecha final (AAAA-MM-DD): ")
    res = l.req_5(control, f_costo, f_inicial, f_final)
    print("\n--- Resultado Requerimiento 5 ---")
    print(f"Tiempo de ejecución (ms): {res['tiempo de ejecucion (ms)']}")
    print(f"Filtro seleccionado del costo: {res['filtro']}")
    print(f"Trayectos que cumplen el filtro: {res['total de viajes filtrados']}")
    print(f"Franja Horaria: {res["franja horaria"]}")
    print(f"Costo total promedio(USD): {res['costo promedio (USD)']}")
    print(f"Total de viajes en la franja: {res["total de viajes en la franja"]}")
    print(f"Duracion promedio de los trayectos: {res["duracion promedio (min)"]}")
    print(f"# de pasajeros promedio: {res['pasajeros promedio']}")   
    print(f"Costo maximo (USD): {res['costo maximo (USD)']}") 
    print(f"Costo minimo (USD): {res['costo minimo (USD)']}") 
    print("---------------------------------\n")


def print_req_6(control):
     
    b_inicio = input("Ingrese el barrio de inicio: ")
    f_inicial = input("Ingrese la fecha inicial (AAAA-MM-DD): ")
    f_final = input("Ingrese la fecha final (AAAA-MM-DD): ")
    res = l.req_6(control, b_inicio, f_inicial, f_final)
    print("\n--- Resultado Requerimiento 6 ---")
    print(f"Tiempo de ejecución (ms): {res['tiempo de ejecucion (ms)']}")
    print(f"Trayectos que cumplen el filtro: {res['total de viajes filtrados']}")
    print(f"Distancia promedio de los trayectos: {res["distancia promedio (km)"]}")
    print(f"Duracion promedio de los trayectos: {res["duracion promedio (min)"]}")
    print(f"Barrio mas frecuentado: {res['barrio destino mas frecuente']}")   
    print("\nMedios de pago:")
    for pago in res["pagos"]:
        print("Tipo:", pago["tipo"])
        print("  Cantidad de viajes:", pago["cantidad de viajes"])
        print("  Precio promedio (USD):", round(pago["precio promedio (USD)"], 2))
        print("  ¿Es el más usado?:", "Sí" if pago["¿Es el mas usado?"] else "No")
        print("  ¿Es el que genera más recaudo?:", "Sí" if pago["¿Es el que genera más recaudo?"] else "No")
        print("  Tiempo promedio (min):", round(pago["tiempo promedio (min)"], 2))
        print()
    print("---------------------------------\n")

def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            _,tiempo,total,menor_dist,mayor_dist,primeros,ultimos = load_data(control)
            print("Tiempo de carga (ms): " + str(tiempo))
            print('Total de trayectos: ' + str(total))
            print("\nTrayecto de menor distancia (distancia > 0.0 millas):")
            print(f"  - Fecha/Hora de inicio: {menor_dist['inicio']}")
            print(f"  - Distancia (millas): {menor_dist['distancia_millas']}")
            print(f"  - Costo total (USD): {menor_dist['costo_total']}")
            print("\nTrayecto de mayor distancia:")
            print(f"  - Fecha/Hora de inicio: {mayor_dist['inicio']}")
            print(f"  - Distancia (millas): {mayor_dist['distancia_millas']}")
            print(f"  - Costo total (USD): {mayor_dist['costo_total']}")
            print("\nPrimeros cinco trayectos cargados:")
            for idx, t in enumerate(primeros, start=1):
                print(f"  #{idx}")
                print(f"    • Inicio: {t['inicio']}")
                print(f"    • Fin: {t['fin']}")
                print(f"    • Duración (min): {t['duracion_min']}")
                print(f"    • Distancia (millas): {t['distancia_millas']}")
                print(f"    • Costo total (USD): {t['costo_total']}")
            print("\nÚltimos cinco trayectos cargados:")
            for idx, t in enumerate(ultimos, start=1):
                print(f"  #{idx}")
                print(f"    • Inicio: {t['inicio']}")
                print(f"    • Fin: {t['fin']}")
                print(f"    • Duración (min): {t['duracion_min']}")
                print(f"    • Distancia (millas): {t['distancia_millas']}")
                print(f"    • Costo total (USD): {t['costo_total']}")
            
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
