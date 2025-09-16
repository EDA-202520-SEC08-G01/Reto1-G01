from datetime import datetime
import math
import time
import csv
import os
from DataStructures import array_list as al
from DataStructures import single_linked_list as sll

csv.field_size_limit(2147483647)
data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    catalog = {
        "taxis" : al.new_list(),
        "neighborhoods" : al.new_list(),
    }
    return catalog
    pass


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    inicio = get_time()   
    
    n_archivo = "Data/" + filename

    archivo = csv.DictReader(open(n_archivo, encoding='utf-8'))    

    for llave in archivo:

        llave["pickup_datetime"] = datetime.datetime.strptime(llave["pickup_datetime"], "%Y-%m-%d %H:%M:%S")
        llave["dropoff_datetime"] = datetime.datetime.strptime(llave["dropoff_datetime"], "%Y-%m-%d %H:%M:%S")
        llave["passenger_count"] = int(llave["passenger_count"])
        llave["trip_distance"] = float(llave["trip_distance"])
        llave["pickup_longitude"] = float(llave["pickup_longitude"])
        llave["pickup_latitude"] = float(llave["pickup_latitude"])
        llave["rate_code"] = int(llave["rate_code"])
        llave["dropoff_longitude"] = float(llave["dropoff_longitude"])
        llave["dropoff_latitude"] = float(llave["dropoff_latitude"])
        llave["payment_type"] = str(llave["payment_type"])
        llave["fare_amount"] = float(llave["fare_amount"])
        llave["extra"] = float(llave["extra"])
        llave["mta_tax"] = float(llave["mta_tax"])
        llave["tip_amount"] = float(llave["tip_amount"])
        llave["tolls_amount"] = float(llave["tolls_amount"])
        llave["improvement_surcharge"] = float(llave["improvement_surcharge"])
        llave["total_amount"] = float(llave["total_amount"])
        
        al.add_last(catalog["taxis"], llave)
        
    filename2 = "Data/nyc-neighborhoods.csv"
    
    archivo2 = csv.DictReader(open(filename2, encoding='utf-8'))

    for llave2 in archivo2:
        llave2["borough"] = str(llave2["borough"])
        llave2["neighborhood"] = str(llave2["neighborhood"])
        llave2["latitude"] = float(llave2["latitude"])
        llave2["longitude"] = float(llave2["longitude"])

        al.add_last(catalog["neighborhoods"], llave2)

    tamanio = catalog["taxis"]["size"]
    
    i = 0
    
    min = al.get_element(catalog["taxis"], 0)

    max = min

    while min["trip_distance"] <= 0.0:
        i +=1
        min = al.get_element(catalog["taxis"], i)

    for valor in range(0, catalog["taxis"]["size"]):
        elem = al.get_element(catalog["taxis"], valor)
        if elem["trip_distance"] < min["trip_distance"] and elem["trip_distance"] > 0.0:
            min = elem
        elif elem["trip_distance"] > max["trip_distance"]:
            max = elem

    mas_corto = (min["pickup_datetime"], min["trip_distance"], min["total_amount"])

    mas_largo = (max["pickup_datetime"], max["trip_distance"], max["total_amount"])
    
    primeros = []
    
    ultimos = []
    
    for i in range(0, 5):

        element = al.get_element(catalog["taxis"], i)

        resta = element["dropoff_datetime"] - element["pickup_datetime"]
        minutos = resta.total_seconds()/60

        info = [element["pickup_datetime"], element["dropoff_datetime"], minutos, element["trip_distance"], element["total_amount"]]
        primeros.append(info)

    for i in range(tamanio-5, tamanio):
        elemento = al.get_element(catalog["taxis"], i)
        
        resta = elemento["dropoff_datetime"] - elemento["pickup_datetime"]
        minutos = resta.total_seconds()/60
        
        info = [elemento["pickup_datetime"], elemento["dropoff_datetime"], minutos, elemento["trip_distance"], elemento["total_amount"]]
        ultimos.append(info)

    
    final = get_time()
    tiempo = delta_time(inicio, final)
    
    retorno = catalog, tiempo, tamanio, mas_corto, mas_largo, primeros, ultimos
    
    return retorno

    pass

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    size = catalog["taxis"]["size"]
    if size > 0 and id < size:
        element = al.get_element(catalog["taxis"], id)
        return element
    pass


def req_1(catalog, pasajeros):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    """
    Calcula información promedio de los trayectos para una cantidad de pasajeros dada.
    Retorno un diccionario con:
      - tiempo_ms
      - total_trayectos
      - prom_duracion_min
      - prom_costo_total
      - prom_dist_millas
      - prom_peajes
      - pago_mas_usado (formato "MEDIO - cantidad")
      - propina_promedio
      - fecha_mas_frecuente (YYYY-MM-DD)
    """
    inicio = get_time()

    n = al.size(catalog["taxis"])

    conteo = 0
    tiempo_prom = 0.0
    costo_total = 0.0
    dist_prom = 0.0
    tolls_prom = 0.0
    tip_prom = 0.0

    pagos = {}     # tipo de pago y cantidad
    fechas = {}

    for i in range(n):
        e = al.get_element(catalog["taxis"], i)
        if e["passenger_count"] == pasajeros:
            conteo += 1

            # duración en minutos
            dur_min = (e["dropoff_datetime"] - e["pickup_datetime"]).total_seconds() / 60.0
            tiempo_prom += dur_min

            # promedios solicitados
            costo_total += e["total_amount"]
            dist_prom  += e["trip_distance"]
            tolls_prom += e["tolls_amount"]
            tip_prom   += e["tip_amount"]

            # pago más usado
            p = e["payment_type"]
            pagos[p] = pagos.get(p, 0) + 1

            # fecha de inicio (solo AAAA-MM-DD, sin horas)
            f = e["pickup_datetime"].strftime("%Y-%m-%d")
            fechas[f] = fechas.get(f, 0) + 1

    if conteo == 0:
        end = get_time()
        return {
            "tiempo_ms": delta_time(inicio, end),
            "total_trayectos": 0,
            "prom_duracion_min": 0.0,
            "prom_costo_total": 0.0,
            "prom_dist_millas": 0.0,
            "prom_peajes": 0.0,
            "pago_mas_usado": "N/A - 0",
            "propina_promedio": 0.0,
            "fecha_mas_frecuente": "N/A"
        }

    # cálculo de máximos (pago y fecha más frecuente)
    pago_top, pago_top_conteo = None, -1
    for k, v in pagos.items():
        if v > pago_top_conteo:
            pago_top, pago_top_cnt = k, v

    fecha_top, fecha_top_cnt = None, -1
    for k, v in fechas.items():
        if v > fecha_top_cnt:
            fecha_top, fecha_top_cnt = k, v

    final = get_time()
    return {
        "tiempo_ms": round(delta_time(inicio, final), 3),
        "total_trayectos": conteo,
        "prom_duracion_min": round(tiempo_prom / conteo, 3),
        "prom_costo_total": round(costo_total / conteo, 3),
        "prom_dist_millas": round(dist_prom / conteo, 3),
        "prom_peajes": round(tolls_prom / conteo, 3),
        "pago_mas_usado": f"{pago_top} - {pago_top_cnt}",
        "propina_promedio": round(tip_prom / conteo, 3),
        "fecha_mas_frecuente": fecha_top
    }
    
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
