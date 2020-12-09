while True:
    num = int(input("Введите время в секундах (для выхода введите 0): "))
    hours = num // 3600
    minutes = (num - hours * 3600) // 60
    print("%02d:%02d:%02d" % (hours, minutes, (num - hours * 3600 - minutes * 60)))
    if num == 0:
        print("Спасибо за ввод")
        break
