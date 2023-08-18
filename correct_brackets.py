from random import randint


def make_line_of_brackets():
    data = ['(', ')']
    brackets_data = []
    for _ in range(randint(10, 20)):
        new_char = ''
        for _ in range(randint(4, 10)):
            new_char += data[randint(0, 1)]
        brackets_data.append(new_char)
    return brackets_data


def choose_correct(data):
    counter = 0
    ans = []
    for char in data:
        rights, lefts = 0, 0
        for sym in char:
            if sym == '(':
                rights += 1
            else:
                lefts += 1
        if char[0] == '(' and char[-1] == ')' and rights == lefts:
            counter += 1
            ans.append(char)
    # print(ans)
    if len(ans) > 0:
        result_data = []
        for item in ans:
            copy_item = item
            while '()' in copy_item:
                copy_item = copy_item.replace('()', '')
                # print(copy_item)
            if len(copy_item) != 0:
                counter -= 1
            else:
                result_data.append(item)
        return (f'User data:\n{data}\nCorrect brackets:\n{result_data}\nCounter:\n{counter}') if counter > 0 else(f'User data:\n{data}\nThere are no correct brackets in user data!')
    else:
        return f'User data:\n{data}\nThere are no correct brackets in user data!'



# def choose_correct_n2(data):
#     structured_data = [[j for j in i] for i in data]
#     print(structured_data)
#     for item in structured_data:
#         for idx in range(len(item)-1):
#             if item[idx] == '(' and item[idx+1] == ')':
#                 item.remove(item[idx])
#                 item.remove(item[idx+1])
#     return item

            
print(choose_correct(make_line_of_brackets()))
