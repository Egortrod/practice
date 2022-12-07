
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
for key in set([*d1.keys(), *d2.keys()]):
    if key in d2.keys():
        r.append({
        "key": key,
        "value": d2[key],
        "type": "exclude"
        })
    if key in d1.keys():
        r.append({
        "key": key,
        "value": d1[key],
        "type": "include"
        })
    if key in d1.keys() and key in d2.keys():
        if d2[key] == d1[key]:
            r.append({
            "key": key, 
            "value": d2[key], 
            "type": "same"
            })

print(r)
