def add_tuple_to_list(lst, tpl):
    lst.append(tpl)
    return lst

def swap_elements_in_tuple_list(lst, index1, index2):
    for i in range(len(lst)):
        lst[i] = list(lst[i])
        lst[i][index1], lst[i][index2] = lst[i][index2], lst[i][index1]
        lst[i] = tuple(lst[i])
    return lst

def check_condition_in_tuple_list(lst, index, condition):
    return [item for item in lst if condition(item[index])]

def find_car_by_model(cars, model):
    return [car for car in cars if car['model'] == model]

def find_car_by_year_range(cars, start_year, end_year):
    return [car for car in cars if start_year <= car['year'] <= end_year]

def find_unique_characters(string):
    return list(set(string))

def take_elements_from_list(lst, indexes):
    return [lst[i] for i in indexes if i < len(lst)]

def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b
