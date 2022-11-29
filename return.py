print(f'Insert amount in KZT:')
idx = float(input())
print(f'Choose currency:\n[1] USD\n[2] EUR\n[3] RUB')
choice = int(input())
if choice == 1:
    print(f'{round((idx/420), 2)} USD')
elif choice == 2:
    print(f'{round((idx/510), 2)} EUR')
elif choice == 3:
    print(f'{round((idx/5.8), 2)} RUB')
elif choice < 1 or choice > 3:
    print(f'Choose correct currency: 1, 2 or 3!')


