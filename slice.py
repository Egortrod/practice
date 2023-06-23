def right(data):
    return data[-1:] + data[:-1]

def left(data):
    return data[1:] + data[:1]

print(right([1, 2, 3]))
print(left([1, 2, 3]))