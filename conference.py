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


def aaaa(timeset):
    begin_times = [i[0] for i in timeset]
    end_times = [i[1] for i in timeset]
    begin_times = sorted(begin_times)
    end_times = sorted(end_times)
    counter = 0
    while len(begin_times) > 0:
        begin_time = begin_times.pop(0)
        end_time = end_times[0]
        if end_time <= begin_time:
            end_times.pop(0)
        else:
            counter += 1
    return counter
    
userdata = [[1, 30], [10, 15], [20, 25]]
print(aaaa(userdata))
    
    
# print(aaa(arr))