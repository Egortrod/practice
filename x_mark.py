def x_mark(user_data):
    source = user_data
    idx_0 = 0
    idx_n = user_data
    space = ' '
    while user_data >= 0:
        print(int(idx_0) * space + '*' + int(idx_n) * (2 * space) + '*')
        idx_0 += 1
        idx_n -= 1
        user_data -= 1
    while user_data <= source:
        print(int(idx_0) * space + '*' + int(idx_n) * (2 * space) + '*')
        idx_0 -= 1
        idx_n += 1
        user_data += 1
#     while user_data > 0:
#         print(idx * ' ' + '*' + ' ' * user_data * 3 + '*')
#         user_data -= 1
#         idx += 2
#     print(idx * ' ' + '*')
x_mark(7)