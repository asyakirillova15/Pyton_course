a = int(input("Введите результат первого дня, км "))
b = int(input("Введите желаемый результат, км "))
counter = 1
while True:
    a *= 1.1
    counter += 1
    if a >= b:
        break
print(counter)
