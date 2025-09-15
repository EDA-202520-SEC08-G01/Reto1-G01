from DataStructures import list_node as ns


def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }
    
    return newlist

def add_first(list, element):
    n = ns.new_single_node(element)
    if list["last"] == None:
        list["last"] = n
    n["next"] = list["first"]
    list["first"] = n
    list["size"] += 1
    return list
    

def add_last(list, element):
    n = ns.new_single_node(element)
    if list["first"] == None:
        list["first"] = n
    if list["last"] == None:
        list["last"] = n
    else:
        list["last"]["next"] = n
        list["last"] = n
    list["size"] += 1
    return list

def size(list):
    return list["size"]

def first_element(list):
    if is_empty(list):
        raise Exception("Error, indexacion fuera de rango: No hay elementos para leer")
    else:
        n = list["first"]
        return n["info"]
    
def last_element(list):
    if is_empty(list):
        raise Exception("Error, indexacion fuera de rango: No hay elementos para leer")
    else:
        n = list["last"]
        return n["info"]

def is_empty(list):
    return list["size"] == 0
    
def get_element(list, pos):
    n = list["first"] # indexacion 0
    for i in range(pos):
        n = n["next"]
    return n

def remove_first(list):
    if is_empty(list):
        raise Exception("Error: Indexación fuera de rango -> list['first'] != NoneType")
    n = list["first"]
    list["first"] = n["next"]
    list["size"] -= 1
    return n["info"]
        
def remove_last(list):
   if is_empty(list):
       raise Exception("Error: Indexación fuera de rango -> list['last'] != NoneType")
   n = list["first"]
   last = list["last"]
   
   if n == last:
       list["first"] = None
       list["last"] = None
       list["size"] = 0
       return last["info"]
   
   while n["next"] == last:
       n = n["next"]

   list["last"] = n
   list["last"]["next"] = None
   list["size"] -= 1
   return last["info"]

def insert_element(list, element, pos):
    if 0 <= pos <= size(list):
       node = ns.new_single_node(element)
       if is_empty(list):
         raise Exception("Error: Indexación fuera de rango -> Solo existe la posicion 0, pero el arreglo esta vacio.")
       node_anterior = list["first"]
       for i in range(pos-1):
            node_anterior = node_anterior["next"]
       node["next"] = node_anterior["next"]
       node_anterior["next"] = node
       return list
    else:
        raise Exception('IndexError: list index out of range') # esto esta en la documentacion de DISC - Data Structures btw
        
        
def is_present(list, element, cmp_function):
    node = ns.new_single_node(element)
    if is_empty(list):
         raise Exception("Error: Indexación fuera de rango -> No existe ningun elemento, el arreglo esta vacio.")
    nodo_buscar = list["first"]
    existe = False
    while nodo_buscar["next"] != None:
        if cmp_function(node["info"], nodo_buscar["info"]) == 0:
            existe = True
        nodo_buscar = nodo_buscar["next"]
        index += 1
    if existe:
        return index
    else:
        return -1
    
    
def delete_element(list, pos):
    if 0 <= pos <= size(list):
        if is_empty(list):
           raise Exception("Error: Indexación fuera de rango -> No se puede borrar elementos si no existe ninguno que borrar.")
        n_anterior = list["first"]
    
        for i in range(pos-1):
            n_anterior = n_anterior["next"]
            
        if n_anterior["next"] == None:
            list["first"] = None
            list["Last"] = None
            list["Size"] = 0
            return list
        else:
            n_borrar = n_anterior["next"]
            n_anterior["next"] = n_borrar["next"]
            list["size"] -= 1
            return list
    else:
        raise Exception('IndexError: list index out of range') # esto esta en la documentacion de DISC - Data Structures btw x2
        
def change_info(list, pos, new_info):
    if 0 <= pos <= size(list):
        if is_empty(list):
            raise Exception("Error: Indexación fuera de rango -> No se puede borrar elementos si no existe ninguno que borrar.")
        n_cambio = list["first"]
        for i in range(pos):
            n_cambio = n_cambio["next"]
        n_cambio["info"] = new_info
        return list
    else:
        raise Exception('IndexError: list index out of range') # esto esta en la documentacion de DISC - Data Structures btw x3

def exchange(list, pos1, pos2):
        if not(0 <= pos1 <= size(list) and 0 <= pos2 <= size(list)):
            raise Exception('IndexError: list index out of range') # esto esta en la documentacion de DISC - Data Structures btw x3
        if is_empty(list):
            raise Exception("Error: Indexación fuera de rango -> No se puede borrar elementos si no existe ninguno que borrar.")
        enc_p1_prev = list["first"]
        enc_p2_prev = list["first"]
        for i in range(pos1-1):
            enc_p1_prev = enc_p1_prev["next"]
        for i in range(pos2-1):
            enc_p2_prev = enc_p2_prev["next"]
        
        p1 = enc_p1_prev["next"]
        p2 = enc_p2_prev["next"]
        
        if p1["next"]==None:
            p1["next"] = p2["next"]
            p2["next"] = None
        elif p2["next"]==None:
            p2["next"] = p1["next"]
            p1["next"] = None
        
        enc_p2_prev["next"] = p1
        enc_p1_prev["next"] = p2
        return list

def sub_list(list, pos, num_elements):
    if not(0 <= pos <= size(list)):
            raise Exception('IndexError: list index out of range') # esto esta en la documentacion de DISC - Data Structures btw x3
    if is_empty(list):
            raise Exception("Error: Indexación fuera de rango -> No se puede borrar elementos si no existe ninguno que borrar.")
    sub_list = new_list()
    ini_lista = list["first"]
    for i in range(pos):
        ini_lista = ini_lista["next"]
    
    sub_list["first"] = ini_lista
    sub_list["last"] = list["last"]
    sub_list["size"] = num_elements
    return sub_list
    