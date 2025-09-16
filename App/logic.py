from datetime import datetime
import math
from datetime import datetime
import math
import time
import csv
import os
from DataStructures import array_list as al
from DataStructures import single_linked_list as sll

csv.field_size_limit(2147483647)
data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'
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

        llave["pickup_datetime"] = datetime.strptime(llave["pickup_datetime"], "%Y-%m-%d %H:%M:%S")
        llave["dropoff_datetime"] = datetime.strptime(llave["dropoff_datetime"], "%Y-%m-%d %H:%M:%S")
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
    
    archivo2 = csv.DictReader(open(filename2, encoding='utf-8'), delimiter=";")

    for llave2 in archivo2:
        llave2["borough"] = llave2["borough"]
        llave2["neighborhood"] = llave2["neighborhood"]
        lat_str = llave2["latitude"].replace(',', '.')
        lon_str = llave2["longitude"].replace(',', '.')
        llave2["latitude"] = float(lat_str)
        llave2["longitude"] = float(lon_str)

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


def req_2(catalog, m_pago):

    inicio = get_time()
    
    t_metodos = al.size(catalog["taxis"])
    filtrados = 0
    dur_prom = 0 # Minutos
    c_prom = 0 # Dolares
    dis_prom = 0 # Millas
    c_peajes = 0
    propina_prom = 0
    frecuencia_pa = {}
    frecuencia_fech = {}
    
    for i in range(t_metodos):
        pago = al.get_element(catalog["taxis"],i)
        if pago["payment_type"] == m_pago:
            filtrados += 1
            dur_prom += (pago["dropoff_datetime"] - pago["pickup_datetime"]).total_seconds() /60
            c_prom += pago["total_amount"]
            dis_prom += pago["trip_distance"]
            c_peajes += pago["tolls_amount"]
            propina_prom += pago["tip_amount"]
            pasajero = pago["passenger_count"]
            fecha = pago["dropoff_datetime"].strftime("%Y-%m-%d")
            
            frecuencia_pa[pasajero] = frecuencia_pa.get(pasajero, 0) + 1
            frecuencia_fech[fecha] = frecuencia_pa.get(pasajero, 0 ) + 1
            
    if filtrados == 0: # hora de procesar toda esta vaina jsjs
        fin = get_time()
        return_t = {
            "Tiempo de ejecucion (ms)": delta_time(inicio,fin),
            "Trayectos totales": t_metodos,
            "Trayectos filtrados": 0,
            "Duracion promedio p/trayecto (min)": 0.0,
            "Coste promedio (USD)": 0.0,
            "Distancia promedio (millas)": 0.0,
            "Coste de peaje promedio": 0.0,
            "Propina promedio": 0.0,
            "Pasajero mas frecuente": "N/A",
            "Frecuencia de fecha": "N/A" 
        }
    elif filtrados > 0:
        fin = get_time()
        
        p_frecuente = None
        frecuencia_p = 0
        for i in frecuencia_pa:
            if frecuencia_pa[i] > frecuencia_p:
                p_frecuente = i
                frecuencia_p = frecuencia_pa[i]
        
        fechamas_frecuente = None
        frecuencia_f = 0
        for i in frecuencia_fech:
            if frecuencia_fech[i] > frecuencia_f:
                fechamas_frecuente = i
                frecuencia_f = frecuencia_fech[i]
        
        return_t = {
            "Tiempo de ejecucion (ms)": delta_time(inicio,fin),
            "Trayectos totales": t_metodos,
            "Trayectos filtrados": filtrados,
            "Duracion promedio p/trayecto (min)": dur_prom/t_metodos,
            "Coste promedio (USD)": c_prom/t_metodos,
            "Distancia promedio (millas)": dis_prom/t_metodos,
            "Coste de peaje promedio": c_peajes/t_metodos,
            "Propina promedio": propina_prom/t_metodos,
            "Pasajero mas frecuente": p_frecuente,
            "Frecuencia de fecha":  fechamas_frecuente
        }  
    else:
        raise Exception("Error: hay algo que no funciona en la carga de datos del req 2")
    return return_t

def req_3(catalog, pago_min, pago_max):
    
    inicio = get_time()

    totalviajes = al.size(catalog["taxis"])
    filtrados = 0
    suma_duracion_min = 0
    suma_total = 0
    suma_distancia = 0
    suma_peajes = 0
    suma_propinas = 0

    frec_pasajeros = {}
    frec_fechas = {}

    for i in range(totalviajes):

        viaje = al.get_element(catalog["taxis"], i)
        costo = viaje["total_amount"]

        if costo is not None and pago_min <= costo <= pago_max:
            filtrados += 1

            duracion_min = (viaje["dropoff_datetime"] - viaje["pickup_datetime"]).total_seconds() / 60
            suma_duracion_min += duracion_min

            suma_total += costo
            suma_distancia += viaje["trip_distance"]
            suma_peajes += viaje["tolls_amount"]
            suma_propinas += viaje["tip_amount"]
            pasajeros = viaje["passenger_count"]

            if pasajeros in frec_pasajeros:
                frec_pasajeros[pasajeros] += 1
            else:
                frec_pasajeros[pasajeros] = 1

            fecha_final = viaje["dropoff_datetime"].strftime("%Y-%m-%d")
            if fecha_final in frec_fechas:
                frec_fechas[fecha_final] += 1
            else:
                frec_fechas[fecha_final] = 1

            if filtrados > 0:
                promedio_duracion = suma_duracion_min / filtrados
                promedio_costo = suma_total / filtrados
                promedio_distancia = suma_distancia / filtrados
                promedio_peajes = suma_peajes / filtrados
                promedio_propinas = suma_propinas / filtrados

                pasajeros_mas_frec = None
                frecuencia_pasajeros = 0
                for clave in frec_pasajeros:
                    curr_frec = frec_pasajeros[clave]
                    if curr_frec > frecuencia_pasajeros:
                        frecuencia_pasajeros = curr_frec
                        pasajeros_mas_frec = clave

                fecha_final_mas_frec = None
                frecuencia_fecha_mayor = 0
                for fecha in frec_fechas:
                    curr_frec_fecha = frec_fechas[fecha]
                    if curr_frec_fecha > frecuencia_fecha_mayor:
                        frecuencia_fecha_mayor = curr_frec_fecha
                        fecha_final_mas_frec = fecha


            else:
                promedio_duracion = 0.0
                promedio_costo = 0.0
                promedio_distancia = 0.0
                promedio_peajes = 0.0
                promedio_propinas = 0.0
                pasajeros_mas_frec = None
                frecuencia_pasajeros = 0
                fecha_final_mas_frec = None

    final = get_time()
    tiempo = delta_time(inicio, final)

    retorno = {
        "tiempo de ejecucion (ms)": tiempo,
        "total de viajes válidos": filtrados,
        "promedio duración (min)": promedio_duracion,
        "promedio costo (USD)": promedio_costo,
        "promedio distancia (millas)": promedio_distancia,
        "promedio pago peajes": promedio_peajes,
        "num pasajeros mas frecuente": pasajeros_mas_frec,
        "promedio propinas": promedio_propinas,
        "fecha final mas frecuente": fecha_final_mas_frec
    }

    return retorno

def haversine(lat1, lon1, lat2, lon2):
        R = 6371.0 # radio tierra (km)
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a))
        return R * c

def req_4(catalog, f_costo, f_inicial, f_final):
    
    def barrio_mas_cercano(lat, lon, lista_barrios):
        mejor_barrio = None
        mejor_distancia = float('inf')
        total_barrios = al.size(lista_barrios)

        for i in range(total_barrios):
            barrio = al.get_element(lista_barrios, i)
            distancia = haversine(lat, lon, barrio["latitude"], barrio["longitude"])
            if distancia < mejor_distancia:
                mejor_distancia = distancia
                mejor_barrio = barrio["neighborhood"]

        return mejor_barrio
    
    inicio = get_time()

    fecha_inicial = datetime.strptime(f_inicial, "%Y-%m-%d").date()
    fecha_final = datetime.strptime(f_final, "%Y-%m-%d").date()

    totalviajes = al.size(catalog["taxis"])
    filtrados = 0

    combinaciones = {}

    for i in range(totalviajes):
        viaje = al.get_element(catalog["taxis"], i)
        pkup_date = viaje["pickup_datetime"].date()

        if fecha_inicial <= pkup_date <= fecha_final:
            filtrados += 1
        
        origen = barrio_mas_cercano(viaje["pickup_latitude"], viaje["pickup_longitude"], catalog["neighborhoods"])
        destino = barrio_mas_cercano(viaje["dropoff_latitude"], viaje["dropoff_longitude"], catalog["neighborhoods"])

        if origen != destino:
            clave = (origen, destino)

            duracion = (viaje["dropoff_datetime"] - viaje["pickup_datetime"]).total_seconds() / 60

            if clave not in combinaciones:
                combinaciones[clave] = {
                    "distancia": 0.0,
                    "duracion": 0.0,
                    "costo": 0.0,
                    "conteo": 0
                }
            
            combinaciones[clave]["distancia"] += viaje["trip_distance"]
            combinaciones[clave]["duracion"] += duracion
            combinaciones[clave]["costo"] += viaje["total_amount"]
            combinaciones[clave]["conteo"] += 1

    barrio_origen = barrio_destino = None
    distancia_promedio = duracion_promedio = costo_promedio = 0.0

    if len(combinaciones) > 0:
        if f_costo == "MAYOR":
            m_costo = float('-inf')
        else:
            m_costo = float('inf')
        
        for clave in combinaciones:
            datos = combinaciones[clave]
            conteo = datos["conteo"]
            costo_prom = datos["costo"] / conteo

        if (f_costo == "MAYOR" and costo_prom > m_costo) or (f_costo == "MENOR" and costo_prom < m_costo):
                m_costo = costo_prom
                barrio_origen, barrio_destino = clave
                distancia_promedio = datos["distancia"] / conteo
                duracion_promedio = datos["duracion"] / conteo
                costo_promedio = costo_prom
    
    final = get_time()
    tiempo = delta_time(inicio, final)

    retorno = {
        "tiempo de ejecucion (ms)": tiempo,
        "filtro": f_costo,
        "total de viajes filtrados": filtrados,
        "barrio de origen": barrio_origen,
        "barrio de destino": barrio_destino,
        "distancia promedio (km)": distancia_promedio,
        "duracion promedio (min)": duracion_promedio,
        "costo promedio (USD)": costo_promedio
    }

    return retorno

def req_5(catalog, f_costo, f_inicial, f_final):

    inicio = get_time()

    f_inicial = datetime.datetime.strptime(f_inicial, "%Y-%m-%d")
    f_final = datetime.datetime.strptime(f_final, "%Y-%m-%d")
    totalviajes = al.size(catalog["taxis"])
    filtrados = 0

    franjas =  {}

    for i in range(totalviajes):
        viaje = al.get_element(catalog["taxis"], i)
        pkup_date = viaje["pickup_datetime"].date()

        if f_inicial <= pkup_date <= f_final:
            filtrados += 1

            hora =  viaje["pickup_datetime"].hour()
            if hora not in franjas:
                franjas[hora] = {
                    "costo_total": 0.0,
                    "conteo": 0,
                    "duracion total": 0.0,
                    "total pasajeros": 0,
                    "costo maximo": float('-inf'),
                    "costo minimo": float('inf')
                }
            duracion = (viaje["dropoff_datetime"] - viaje["pickup_datetime"]).total_seconds() / 60
            costo = viaje["total_amount"]
            pasajeros = viaje["passenger_count"]

            franjas[hora]["costo_total"] += costo
            franjas[hora]["conteo"] += 1
            franjas[hora]["duracion total"] += duracion
            franjas[hora]["total pasajeros"] += pasajeros

            if costo > franjas[hora]["costo maximo"]:
                franjas[hora]["costo maximo"] = costo
            if costo < franjas[hora]["costo minimo"]:
                franjas[hora]["costo minimo"] = costo

            mejor_hora = None
            if f_costo == "MAYOR":
                mejor_costo_prom = float('-inf')
            else:
                mejor_costo_prom = float('inf')

            for hora in franjas:
                datos = franjas[hora]
                costo_prom = datos["costo_total"] / datos["conteo"]

                if (f_costo == "MAYOR" and costo_prom > mejor_costo_prom) or (f_costo == "MENOR" and costo_prom < mejor_costo_prom):
                    mejor_hora = hora
                    mejor_costo_prom = costo_prom

            datos = franjas[mejor_hora]
            conteo = datos["conteo"]

            final = get_time()
            tiempo = delta_time(inicio, final)

            retorno = {
                "tiempo de ejecucion (ms)": tiempo,
                "filtro": f_costo,
                "total de viajes filtrados": filtrados,
                "franja horaria": str(mejor_hora - (mejor_hora-1)),
                "costo promedio (USD)": datos["costo_total"] / conteo,
                "total de viajes en la franja": conteo,
                "duracion promedio (min)": datos["duracion total"] / conteo,
                "pasajeros promedio": datos["total pasajeros"] / conteo,
                "costo maximo (USD)": datos["costo maximo"],
                "costo minimo (USD)": datos["costo minimo"]
            }

            return retorno
        
def req_6(catalog, b_inicio, f_inicial, f_final):

    def barrio_mas_cercano(lat, lon, lista_barrios):
        mejor_barrio = None
        mejor_distancia = float('inf')
        barrios = al.size(lista_barrios)

        for i in range(barrios):
            barrio = al.get_element(lista_barrios, i)
            distancia = haversine(lat, lon, barrio["latitude"], barrio["longitude"])
            if distancia < mejor_distancia:
                mejor_distancia = distancia
                mejor_barrio = barrio["neighborhood"]

        return mejor_barrio
    
    inicio = get_time()
    fecha_inicial = datetime.datetime.strptime(f_inicial, "%Y-%m-%d")
    fecha_final = datetime.datetime.strptime(f_final, "%Y-%m-%d")
    totalviajes = al.size(catalog["taxis"])
    filtrados = 0

    distancia_km = 0.0
    duracion_min = 0.0

    destinos = {}
    pagos = {}

    for i in range(totalviajes):
        viaje = al.get_element(catalog["taxis"], i)
        pkup_date = viaje["pickup_datetime"].date()
        if fecha_inicial <= pkup_date <= fecha_final:
            origen = barrio_mas_cercano(viaje["pickup_latitude"], viaje["pickup_longitude"], catalog["neighborhoods"])
            if origen == b_inicio:
                filtrados += 1
                dist_km += haversine(viaje["pickup_latitude"], viaje["pickup_longitude"], viaje["dropoff_latitude"], viaje["dropoff_longitude"])
                dur_min += (viaje["dropoff_datetime"] - viaje["pickup_datetime"]).total_seconds() / 60

                destino = barrio_mas_cercano(viaje["dropoff_latitude"], viaje["dropoff_longitude"], catalog["neighborhoods"])

                distancia_km += dist_km
                duracion_min += dur_min

                if destino in destinos:
                    destinos[destino] += 1
                else:
                    destinos[destino] = 1

                metodo_pago = viaje["payment_type"]
                if metodo_pago not in pagos:
                    pagos[metodo_pago] = {
                        "conteo": 0,
                        "total_pagado": 0.0,
                        "total duracion": 0.0
                    }
                pagos[metodo_pago]["conteo"] += 1
                pagos[metodo_pago]["total_pagado"] += viaje["total_amount"]
                pagos[metodo_pago]["total duracion"] += dur_min

        if filtrados == 0:
            fin = get_time()
            tiempo = delta_time(inicio, fin)
            retorno = {
                "tiempo de ejecucion (ms)": tiempo,
                "total de viajes filtrados": filtrados,
                "distancia promedio (km)": 0.0,
                "duracion promedio (min)": 0.0,
                "barrio destino mas frecuente": None,
                "pagos": []
            }
            return retorno
        destino_mas_frec = None
        max = float('-inf')
        for i in destinos:
            x = destinos[i]
            if x > max:
                max = x
                destino_mas_frec = i
        
        metodo_pago_max = None
        max_conteo = float('-inf')
        metodo_recaudo_max = None
        max_recaudo = float('-inf')

        for metodo in pagos:
            if pagos[metodo]["conteo"] > max_conteo:
                max_conteo = pagos[metodo]["conteo"]
                metodo_pago_max = metodo
            if pagos[metodo]["total_pagado"] > max_recaudo:
                max_recaudo = pagos[metodo]["total_pagado"]
                metodo_recaudo_max = metodo
        
        lista_pagos = []
        for metodo in pagos:
            count = pagos[metodo]["conteo"]
            lista_pagos.append({
                "tipo": metodo,
                "cantidad de viajes": count,
                "precio promedio (USD)": pagos[metodo]["total_pagado"] / count,
                "¿Es el mas usado?": metodo == metodo_pago_max,
                "¿Es el que genera más recaudo?": metodo == metodo_recaudo_max,
                "tiempo promedio (min)": pagos[metodo]["total duracion"] / count
            })

        fin = get_time()
        tiempo = delta_time(inicio, fin)

        retorno = {
            "tiempo de ejecucion (ms)": tiempo,
            "total de viajes filtrados": filtrados,
            "distancia promedio (km)": distancia_km / filtrados,
            "duracion promedio (min)": duracion_min / filtrados,
            "barrio destino mas frecuente": destino_mas_frec,
            "pagos": lista_pagos
        }

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
