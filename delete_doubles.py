def ddd(user_list: list) -> list:
    arr = []
    for idx in user_list:
        if idx not in arr:
            arr.append(idx)
    return sorted(arr)
    
    
def dddd(user_list: list) -> list:
    return list(set(user_list))
    
    
print(ddd([1, 3, 2, 2, 3, 3, 3, 2, 2]))
print(dddd([1, 3, 2, 2, 3, 3, 3, 2, 2]))       