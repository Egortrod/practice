from collections import defaultdict


def to_del(data):
    dic = defaultdict(list)
    for index, word in enumerate(data):
        dic[word].append(index)
    out = ''
    for key, item in dic.items():
        out += f'{key}: {item}\n'
    return out[:-1]

user_data = 'abracadabra'
a = to_del(user_data)
print(a)
