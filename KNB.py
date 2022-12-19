from random import randint

arr = ['Камень', 'Ножницы', 'Бумага']
user_idx, ai_idx = 0, 0

while True:
    print(f'Выбор:\n1 - {arr[0]}\n2 - {arr[1]}\n3 - {arr[2]}\n')

    print('Удачной игры!\n')
    loop = 0
    while loop == 0:
        user_input = int(input('Выберите позицию, напишите 1, 2 или 3\n№'))
        if user_input not in range(1, 4):
            print('Введите корректные значения')
        else:
            loop = 1
    print(f'Ваш выбор - {arr[user_input - 1]}!')

    ai_input = randint(1, 3)
    print(f'Выбор компьютера - {arr[ai_input - 1]}!')
    
    if (user_input == 1 and ai_input == 1) or (user_input == 2 and ai_input == 2) or (user_input == 3 and ai_input == 3):
        result = 0
    if (user_input == 1 and ai_input == 2) or (user_input == 2 and ai_input == 3) or (user_input == 3 and ai_input == 1):
        result = 1
        user_idx += 1
    if (user_input == 2 and ai_input == 1) or (user_input == 3 and ai_input == 2) or (user_input == 1 and ai_input == 3):
        result = 2
        ai_idx += 1
        
    arr2 = ['Ничья', 'Победа', 'Поражение']
    print(f'-------------------\nРезультат игры - {arr2[result]}!')
    print(f'-------------------\nСчет матча: {user_idx} - {ai_idx}')
    
    exit_button = input('\nЕсли хотите выйти из игры - напишите exit и нажмите enter\nВ случае продолжения нажмите enter\n')
    if exit_button == 'exit':
        break
        