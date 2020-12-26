with open('text_3.txt', 'r', encoding='utf-8') as list_rates:
    salary_total = 0
    line_ = 0
    line_count = 0
    try:
        for line_ in list_rates.readlines():
            line = line_.split()
            if len(line) == 1:
                raise ValueError("Не указана зарплата")
            if len(line) > 2:
                raise ValueError("Лишние символы в строке")
            try:
                salary = float(line[1])
            except ValueError:
                raise ValueError("Значение зарплаты должно быть числом!")
            if salary < 0:
                raise ValueError("Зарплата должна быть больше ноля!")
            salary_total += salary
            if salary < 20000.0:
                print(line[0])
            line_count += 1
        print(f"Средняя зарплата сотрудников отдела: {salary_total / line_count}")
    except ValueError as error:
        print(f"{error} в строке: {line_}")
