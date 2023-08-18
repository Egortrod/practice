def create_data():
    idx = 0
    data = [str(i) for i in range(1000000)]
    while idx != 100000:
        while len(data[idx]) != 6:
            data[idx] = '0' + data[idx]
        idx += 1
    return data


def find_lucky(data):
    lucky_numbers = []
    counter = 0
    for number in data:
        if int(number[0]) + int(number[1]) + int(number[2]) == int(number[3]) + int(number[4]) + int(number[5]):
            lucky_numbers.append(number)
            counter += 1
    return f'There are {counter} lucky tickets exists!'
 

print(find_lucky(create_data()))