from random import *
import time

# duration = 0
data = [randint(160, 190) for _ in range(6)]
unload = round(randint(167000, 200000)/100000, 2)
upload_per_90 = 14
upload_per_50 = 7.78
print(data)

def find_min(user_arr):
    return min(user_arr)

def filling(user_arr):
    duration = 0
    while True:
        for i, j in enumerate(user_arr):
            user_arr[i] -= unload
        # print(user_arr)
        arr = []
        minimum = min(user_arr)
        print(f'minimum =', round(minimum, 2))
        for elem in user_arr:
            if elem != minimum:
                arr.append(round(elem, 2))
            elif elem == minimum:
                if elem / 200 >= 0.9:
                    arr.append(round(elem + upload_per_50, 2))
                    duration += 50
                    curr_time = 50
                elif elem / 200 < 0.9:
                    arr.append(round(elem + upload_per_90, 2))
                    duration += 90
                    curr_time = 90
        time.sleep(2)
        print(f'duration: {duration/60} min, current time: {curr_time} sec,  {arr}')
        user_arr = arr
        minimum = min(arr)
        
filling(data)




# -----------------------


# from random import *
# import time

# data = [randint(50, 190) for _ in range(6)]
# unload = round(randint(167000, 200000)/1000, 2)
# upload_per_90 = 14
# upload_per_50 = 7.78
# print(data)

# def find_min(user_arr):
#     return min(user_arr)

# def filling(user_arr):
#     while True:
#         for i, j in enumerate(user_arr):
#             user_arr[i] -= unload
#         arr = []
#         minimum = min(user_arr)
#         for elem in user_arr:
#             if elem != minimum:
#                 arr.append(round(elem, 3))
#             if elem == minimum:
#                 arr.append(round(elem + 2, 3))
#         time.sleep(2)
#         print(arr)
#         user_arr = arr
#         minimum = min(arr)
        
# filling(data)