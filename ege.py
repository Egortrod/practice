# for i in range(185311, 185331):
#     lists = []
#     # print (i)
#     for j in range(1, i+1):
#         if i % j == 0:
#             lists.append(j)
#             if len(lists) == 4:
#                 if lists[-1] == i:
#                     print(f'Для числа {i} список: {lists}')



for num in range(185311, 185331):
    deliteli = []
    for d in range(1, int(num**0.5) + 1):
        if num % d == 0:
            deliteli.append(d)
            if num//d != d:
                deliteli.append(num//d)
    if len(deliteli) == 4:
        deliteli.sort()
        print(deliteli[0],deliteli[1],deliteli[2],deliteli[3])