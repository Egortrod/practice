# def find_local_max(data):
#     data1 = []
#     for i, j in enumerate(data[1:-1]):
#         if j > data[i-1] and j > data[i+1]:
#             data1.append(j)
#     return data1


def find_local_max(data):
    data1 = []
    i = 1
    while i < len(data) - 1:
        if data[i] > data[i-1] and data[i] > data[i+1]:
            data1.append(data[i])
        i += 1
    return data1


user_list = [1, 3, 5, 8, 7, 9, 0, 5, 4, 8, 7]
print(find_local_max(user_list))


# data = [1, 3, 5, 8, 7, 9, 0, 5, 4]

# for i, j in enumerate(data[1:-1]):
#     print(f'{i} : {j}')