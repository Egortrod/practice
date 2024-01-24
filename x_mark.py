def x_mark_first(user_data):
    source, idx_n = user_data, user_data
    idx_0 = 0
    space = ' '
    while user_data > 0:
        print(idx_0 * space + '*' + idx_n * space * 2 + '*')
        idx_0 += 1
        idx_n -= 1
        user_data -= 1
    while user_data <= source:
        print(idx_0 * space + '*' + idx_n * space * 2 + '*')
        idx_0 -= 1
        idx_n += 1
        user_data += 1
    print('\n')

def x_mark_second(user_data):
    source, idx_n = user_data, user_data
    idx_0 = 0
    space = ' '
    while user_data > 0:
        print(idx_0 * space + '*' + (2 * idx_n - 1) * space + '*')
        idx_0 += 1
        idx_n -= 1
        user_data -= 1
    print(idx_0 * space + '*')
    idx_0 -= 1
    idx_n += 1
    user_data += 1
    while user_data <= source:
        print(idx_0 * space + '*' + (2 * idx_n - 1) * space + '*')
        idx_0 -= 1
        idx_n += 1
        user_data += 1
    print('\n')


def x_mark_third(user_data):
    source, idx_n = user_data, user_data
    idx_0, multiply = 0, 2
    space = ' '
    while user_data > 0:
        print(idx_0 * space * multiply + '*' + (2 * idx_n * multiply - 1) * space + '*')
        idx_0 += 1
        idx_n -= 1
        user_data -= 1
    print(idx_0 * space * multiply + '*')
    idx_0 -= 1
    idx_n += 1
    user_data += 1
    while user_data <= source:
        print(idx_0 * space * multiply + '*' + (2 * idx_n * multiply - 1) * space + '*')
        idx_0 -= 1
        idx_n += 1
        user_data += 1
    print('\n')


x_mark_first(3)
x_mark_second(3)
x_mark_third(3)
