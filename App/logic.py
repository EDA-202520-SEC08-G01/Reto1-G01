from datetime import datetime
import time
import csv
import os
from DataStructures import array_list as al
from DataStructures import single_linked_list as sll

csv.field_size_limit(2147483647)
data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

def new_logic():
    
    catalog = {
        "taxis" : al.new_list(),
        "neighborhoods" : al.new_list(),
    }
    return catalog


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
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


# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    
    size = catalog["taxis"]["size"]
    if size > 0 and id < size:
        element = al.get_element(catalog["taxis"], id)
        return element

def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
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
