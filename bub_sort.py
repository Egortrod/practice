def bub_sort(user_data):
    cont = True
    while cont:
        cont = False
        for idx in range(len(user_data)-1):
            if user_data[idx] > user_data[idx+1]:
                user_data[idx], user_data[idx+1] = user_data[idx+1], user_data[idx]
                cont = True
    return user_data
    

from random import randint

user_data = [randint(1, 50) for _ in range(20)]
print(f'user arr: {user_data}')
print(f'sorted arr: {bub_sort(user_data)}')
        