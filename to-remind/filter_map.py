#filter and map together

def filter_map(func, iterable):   #user
    result = []
    for item in iterable:
        result.append(func(item))
    new_result = []
    for item in result:
        if item[0] == True:
            new_result.append(item[1])
    return new_result

def filter_map(function, items):   #hexlet
    result = []
    for item in items:
        keep, value = function(item)
        if keep:
            result.append(value)
    return result