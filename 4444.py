try:
    x1 = int(input('Введите координату x1 - '))
    y1 = int(input('Введите координату y1 - '))
    x2 = int(input('Введите координату x2 - '))
    y2 = int(input('Введите координату y2 - '))

    if x1 > 8 or x2 > 8 or y1 > 8 or y2 > 8:
        print('Значения должны быть в интервале от 1 до 8!')
        exit()
    if x1 < 1 or x2 < 1 or y1 < 1 or y2 < 1:
        print('Значения должны быть в интервале от 1 до 8!')
        exit()

    if (x1 + y1 + x2 + y2) % 2 == 0:
        print('------------------\nЗаданные клетки одного цвета\n------------------')
    else:
        print('------------------\nЗаданные клетки разного цвета\n------------------')

except ValueError:
    print(f'Ошибка {ValueError}, введите валидные значения x и y!')
    exit()

except NameError:
    print(f'Ошибка {NameError}, введите валидные значения x и y!')
    exit()

print('За какую фигуру вы будете выполнять ход?\n1 - Ладья\n2 - Король')

try:
    user_input = int(input())

except ValueError:
    print(f'Ошибка {ValueError}, введите валидные значение: 1 или 2!')
    exit()

if user_input == 1:
    if x1 == x2 or y1 == y2:
        print('Ладья побьет фигуру за 1 ход')
    else:
        print('Ладья не побьет фигуру за 1 ход')

if user_input == 2:
    if abs(x1 - x2) >= 1 and abs(y1 - y2) >= 1:
        print('Король побьет фигуру за 1 ход')
    else:
        print('Король не побьет фигуру за 1 ход')
    
if user_input not in (1, 2):
    print('Выберите корректное значение фигуры: 1 или 2!')