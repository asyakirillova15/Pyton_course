month = input("Введите номер месяца: ")
while int(month) <= 0 or int(month) > 12:
    month = input("Введите номер месяца от 1 до 12: ")

year = {'12': 'winter', '1': 'winter', '2': 'winter', '3': 'spring', '4': 'spring', '5': 'spring', '6': 'summer',
        '7': 'summer', '8': 'summer', '9': 'autumn', '10': 'autumn', '11': 'autumn'}
for el in year.keys():
    print(year.get(month))
    break
month_y = int(input("Введите номер месяца: "))
while month_y <= 0 or month_y > 12:
    month_y = int(input("Введите номер месяца от 1 до 12: "))
list_year = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
for num in list_year:
    print(list_year[month_y - 1])
    break
