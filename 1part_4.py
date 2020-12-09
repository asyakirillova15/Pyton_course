num = int(input("Введите целое положительное число: "))
while num <= 0:
    num = int(input("Обязательно положительное число!: "))

max_value = 0
while num != 0:
    last = num % 10
    num = num // 10
    if last > max_value:
        max_value = last

print(max_value)
