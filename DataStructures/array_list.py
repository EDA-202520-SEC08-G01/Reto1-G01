def new_list():
    
    new_list = {
        "elements": [],
        "size": 0,
    }
    return new_list

def get_element(my_list, index):
    
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):
    
    size = my_list["size"]
    if size == 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(info, element) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1

def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    
def size(my_list):
    return my_list["size"] 

def first_element(my_list):
    if my_list["size"] > 0:
        return my_list["elements"][0]
    else:
        return None

def last_element(my_list):
    if my_list["size"] > 0:
        return my_list["elements"][-1]
    else:
        return None

def remove_first(my_list):
      if my_list["size"] == 0:
        return "IndexError: list index out of range"
      eliminado = my_list["elements"][0]
      del my_list["elements"][0]
      my_list["size"] -= 1
      return eliminado

def remove_last(my_list):
    if my_list["size"] == 0:
        return "IndexError: list index out of range"
    else:
        eliminado = my_list["elements"][-1]
        del my_list["elements"][-1]
        my_list["size"] -= 1
        return eliminado

def insert_element(my_list, pos, element):
    if pos < 0 or pos >= my_list["size"]:
        return "IndexError: list index out of range"
    else:
        my_list["elements"].insert(pos, element)
        my_list["size"] += 1 
        return my_list

def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= my_list["size"]:
        return "IndexError: list index out of range"
    my_list["elements"][pos] = new_info
    return my_list
        
def exchange(my_list, pos_1, pos_2):
    if (pos_1 < 0 or pos_1 >= my_list["size"]) or (pos_2 < 0 or pos_2 >= my_list["size"]):
        return "IndexError: list index out of range"
    
    my_list["elements"][pos_1], my_list["elements"][pos_2] = (
        my_list["elements"][pos_2], 
        my_list["elements"][pos_1]
    )
    
    return my_list
        
def sub_list(my_list, pos_i, num_elements):
    if pos_i < 0 or pos_i >= my_list["size"]:
        return "IndexError: list index out of range"
    
    end_pos = pos_i + num_elements
    if end_pos > my_list["size"]:
        end_pos = my_list["size"]
    
    sub_elements = my_list["elements"][pos_i:end_pos]
    
    return {
        "size": len(sub_elements),
        "elements": sub_elements
    }
    
    
def is_empty(my_list):
    return my_list["size"] == 0

def delete_element(my_list, pos):
    if pos < 0 or pos >= my_list["size"]:
        return "IndexError: list index out of range"
    del my_list["elements"][pos]
    my_list["size"] -= 1
    return my_list

