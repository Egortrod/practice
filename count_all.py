def count_all(data):               # user
    dic = {}
    for i in data:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic.update({i: 1})
    return dic


def count_all(items):              # hexlet
    counters = {}
    for item in items:
        counters[item] = counters.get(item, 0) + 1
    return counters