
# def diff (arr1, arr2):
#     diff_dic = []
#     for index in arr1:
#         for index1 in arr2:
#             if index == index1:
#                 diff_dic.append(index)

#     return diff_dic

# print(diff(text1, text2))



# diffkeys = [k for k in dict1 if dict1[k] != dict2[k]]

# for k in diffkeys:
#     print (k, ':', dict1[k], '->', dict2[k])


# dict1 = {
#   "host": "hexlet.io",
#   "timeout": 50,
#   "proxy": "123.234.53.22",
#   "follow": "false"
# }
# dict2 = {
#   "timeout": 20,
#   "verbose": "true",
#   "host": "hexlet.io"
# }

# def dict_compare(d1, d2):
#     d1_keys = set(d1.keys())
#     d2_keys = set(d2.keys())
#     intersect_keys = d1_keys.intersection(d2_keys)
#     added = d1_keys - d2_keys
#     removed = d2_keys - d1_keys
#     modified = {o : (d1[o], d2[o]) for o in intersect_keys if d1[o] != d2[o]}
#     same = set(o for o in intersect_keys if d1[o] == d2[o])
#     for i in added, removed, modified, same:
#         print(i)

# dict_compare(dict1, dict2),


# r = []
# for key in set([*d1.keys(), *d2.keys()]):
#     if key in d2.keys():
#         r.append({
#         "key": key,
#         "value": d2[key],
#         "type": "+"
#         })
#     if key in d1.keys():
#         r.append({
#         "key": key,
#         "value": d1[key],
#         "type": "-"
#         })
#     if key in d1.keys() and key in d2.keys():
#         if d2[key] == d1[key]:
#             r.append({
#             "key": key, 
#             "value": d2[key], 
#             "type": "="
#             })

# print(r)

d1 = {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": "false"
}
d2 = {
  "timeout": 20,
  "verbose": "true",
  "host": "hexlet.io"
}

r = []
for key in sorted(set([*d1.keys(), *d2.keys()])):
    if key in d1.keys() and key in d2.keys():
      if d2[key] == d1[key]:
            r.append({
            "key": key, 
            "value": d2[key], 
            "type": " "
            })     
    if key in d2.keys():
        r.append({
        "key": key,
        "value": d2[key],
        "type": "+"
        })
    if key in d1.keys():
        r.append({
        "key": key,
        "value": d1[key],
        "type": "-"
        })


for i in r:
  print(i['type'], i['key'], ':', i['value'])


# d1 = {
#   "host": "hexlet.io",
#   "timeout": 50,
#   "proxy": "123.234.53.22",
#   "follow": "false"
# }
# d2 = {
#   "timeout": 20,
#   "verbose": "true",
#   "host": "hexlet.io"
# }

# d3 = [{'key':'key1', 'value':'value1', 'type':' '}, {'key', 'value', 'type' : '-'}, {    'type' : '-'}, {'type' : '+'}]


# for index in dict.index():
  

def generate_diff(data1: dict, data2: dict):
    diff = []
    for key in sorted(set([*data1.keys(), *data2.keys()])):
        if key in data1.keys() and key in data2.keys():
            if data1[key] == data2[key]:
                diff.append({
                    "key": key,
                    "value": data1[key],
                    "type": ' '
                })
            elif data1[key] != data2[key]:
                diff.append({
                    "key": key,
                    "value": data1[key],
                    "type": '-'
                })
                diff.append({
                    "key": key,
                    "value": data2[key],
                    "type": '+'
                })
        if key in data1.keys() and key not in data2.keys():
            diff.append({
                "key": key,
                "value": data1[key],
                "type": '-'
            })
        if key not in data1.keys() and key in data2.keys():
            diff.append({
                "key": key,
                "value": data2[key],
                "type": '+'
            })
    result = []
    for i in key:
      result += i


text1 = {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": "false"
}
text2 = {
  "timeout": 20,
  "verbose": "true",
  "host": "hexlet.io"
}
print(generate_diff(text1, text2))