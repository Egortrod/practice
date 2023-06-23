def find_index(data, symbol):
    for index, word in enumerate(data):
        if word == symbol:
            return index

print(find_index('12345', '5'))

def second_index(data, symbol):
    iterator = iter(data)
    first = find_index(iterator, symbol)
    if first is None:
        return first
    second = find_index(iterator, symbol)
    if second is not None:
        return first + second + 1

print(second_index('12123', '3'))