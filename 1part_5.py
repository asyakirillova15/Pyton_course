profit = int(input("Введите значение выручки,$ "))
lose = int(input("Введите значение издержек,$ "))
result = profit - lose
rentabl = ""
if profit == lose:
    print("Вы ничего не заработали, но и не проиграли")
elif profit > lose:
    print(f"Вы получили прибыль: {result}$!")
else:
    print(f"Вы ушли в минус на: {-result}$!")
if result > 0:
    rentabl = result /  profit
    print("Рентабельность %.2f" %rentabl)
    profit_one = result // int(input("Введите количество сотрудников: "))
    print("Прибыль фирмы в расчете на одного сотрудника,$ %.2f" %profit_one)

