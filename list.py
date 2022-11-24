
def sort_list(lists):
    new_list = []
    for i in lists:
        if i >= 55:
            new_list.append(i)
    return new_list

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(sort_list(a))