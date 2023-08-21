arr = [[0,30],[5,10],[15,20]]


def aaa(user_arr):
    data = []
    for i in user_arr:
        data.append([idx for idx in range(i[0], i[1] + 1)])
    data.sort(key=len)
    idxx, counter = 0, 0
    filtered = data[0]
    for lis in data[1:]:
        for num in lis:
            if num in filtered:
                counter += 1
                continue
        idxx += 1
        filtered.append(data[idxx])
    return counter
        
            
    # return data
    
    
print(aaa(arr))