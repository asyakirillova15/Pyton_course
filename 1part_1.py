name = input("Ваше имя: ")
surname = input("Ваша фамилия: ")
print(f"Добро пожаловать в нашу систему, {name} {surname}!")
years = int(input("Год вашего рождения: "))
age = 2020 - years
print(f"В этом году вам исполняется {age}")
value = input(f"{name}, купи слона ")
while True:
    if value == "":
        value = input(f"Все молчат,  {name}, а ты купи слона\n ")
    elif value == "ок":
        print(f"Круто, {name}, ты купил слона")
        break
    else:
        value = input(f"Все говорят {value}, а ты купи слона\n ")
