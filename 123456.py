input_month = str(input('Введите месяц: ').lower())
number_if_day = int(input('Введите день месяца: '))
months1 = ['январь', 'март', 'май', 'июль', 'август', 'октябрь', 'декабрь']
months2 = ['апрель', 'июнь', 'сентябрь', 'ноябрь']
month3 = ['февраль']
all_months = months1 + months2 + month3

print(f'---------------------------\nВведенная дата - {input_month.capitalize()}, {number_if_day}-е число!')

if input_month not in all_months:
    print('ОШИБКА!\nВведите корректные значения! Месяц указан неверно!')
    exit()

if input_month in months1:
    if number_if_day > 31 or number_if_day < 1:
        print('ОШИБКА!\nВведите корректные значения! День месяца указан неверно!')
        exit()

if input_month in months2:
    if number_if_day > 30 or number_if_day < 1:
        print('ОШИБКА!\nВведите корректные значения! День месяца указан неверно!')
        exit()

if input_month in month3:
    if number_if_day > 28 or number_if_day < 1:
        print('ОШИБКА!\nВведите корректные значения! День месяца указан неверно!')
        exit()

# if input_month not in monthes1 or monthes2 or :
#     if number_if_day > 30 and number_if_day < 1:
#         print('Введите корректные значения!')
#         exit()

if input_month == 'декабрь' or input_month == 'январь' or input_month == 'февраль':
    print('Сезон - Зима!')
elif input_month == 'март' or input_month == 'апрель' or input_month == 'май':
    print('Сезон - Весна!')
elif input_month == 'июнь' or input_month == 'июль' or input_month == 'август':
    print('Сезон - Лето!')
elif input_month == 'сентябрь' or input_month == 'октябрь' or input_month == 'ноябрь':
    print('Сезон - Осень!')    




# -------------------------------------------


# months = [
#   {
#     "name": "январь",
#     "days_amount": 31,
#     "season": 'winter'
#   },
#   {
#     "name": "февраль",
#     "days_amount": 28,
#     "season": 'winter'
#   },
#   {
#     "name": "март",
#     "days_amount": 31,
#     "season": 'autumn'
#   },
#   {
#     "name": "апрель",
#     "days_amount": 30,
#     "season": 'autumn'
#   },
#   {
#     "name": "май",
#     "days_amount": 31,
#     "season": 'autumn'
#   },
#   {
#     "name": "июнь",
#     "days_amount": 30,
#     "season": 'summer'
#   },
#   {
#     "name": "июль",
#     "days_amount": 30,
#     "season": 'summer'
#   },
#   {
#     "name": "август",
#     "days_amount": 31,
#     "season": 'summer'
#   },
#   {
#     "name": "сентябрь",
#     "days_amount": 30,
#     "season": 'fall'
#   },
#   {
#     "name": "октябрь",
#     "days_amount": 31,
#     "season": 'fall'
#   },
#   {
#     "name": "ноябрь",
#     "days_amount": 30,
#     "season": 'fall'
#   },
#   {
#     "name": "декабрь",
#     "days_amount": 31,
#     "season": 'winter'
#   },
# ]

# def validate(day, month, months):
#   rules = {
#     "name": lambda _, m: (m in map(lambda x: x["name"], months)) 
#             or 'This month is invalid! Сheck the values!',
#     "day": lambda d, m: m not in map(lambda x: x["name"], months) 
#            or (m in map(lambda x: x["name"], months) and d <= next(filter(lambda x: x["name"] == m, months))["days_amount"] and d > 0) 
#            or 'This day is invalid! Сheck the values!',
#   }
#   return [*filter(lambda x: x != True, [rules[key](day, month) for key in rules.keys()])]

# def get_season(month, months):
#   return next(filter(lambda m: m["name"] == month, months))["season"]


# month = str(input('Введите месяц: ').lower())
# day = int(input('Введите день месяца: '))
# v = validate(day, month, months)

# if len(v):
#   print("".join(v))
#   exit()

# print(f'The season is {get_season(month, months)}!')