def collect_indexes(user_data):                       #user
    dictionary = {}
    for index, data in enumerate(user_data):
        dictionary.setdefault(data, []).append(index)
    return dictionary


from collections import defaultdict                   #hexlet


def collect_indexes(items):
    result = defaultdict(list)
    for index, item in enumerate(items):
        result[item].append(index)
    return result