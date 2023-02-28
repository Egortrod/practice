def find_words_in_common(data):
    output = ''
    idx = 1
    counter = 0
    while idx < len(data):
        if data[idx] == data[idx-1]:
            counter += 1
        else:
            output += f'({data[idx]}, {counter}) '
            counter = 0
        idx += 1
    return output


def find_words_in_common1(data):
    if not data:
        return ''
    output = ''
    counter = 0
    for j, idx in enumerate(data[1:]):
        # print(data[j])
        if idx == data[j]:
            counter += 1
        else:
            output += f'({data[j]}, {counter+1}) '
            counter = 0
    output += f'({data[j+1]}, {counter+1})'
    return output


def find_words_in_common2(data):
    if not data:
        return ''
        
    occurs = [[data[0], 0]]
    print(occurs)
    for idx in data:
        last_occur = occurs[-1]

        if last_occur[0] == idx:
            last_occur[1] += 1
        else:
            occurs.append([idx, 1])
   
    return " ".join(f"({counter}, {idx})" for idx, counter in occurs)


def find_words_in_common3(data: str) -> str:
    if not data:
        return ''
    idx = data[0]
    counter = 0
    parts = []
    for symbol in data:
        if symbol != idx:
            parts.append(f'({counter}, {idx})')
            idx = symbol
            counter = 1
        else:
            counter += 1
    parts.append(f'({counter}, {idx})')
    return ' '.join(parts)


user_data = [1, 1, 1, 2, 3, 1, 1, 2, 2, 2, 2, 3, 3]
user_data1 = '12222333111145555577'

print(find_words_in_common1(user_data))
