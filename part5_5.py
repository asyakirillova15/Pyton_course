from random import randint

my_list = [randint(-10, 67) for _ in range(10)]
my_str = ' '.join(str(i) for i in my_list)
elem_sum = 0
with open('text_5.txt', 'w+', encoding='utf-8') as numbers_list:
    numbers_list.writelines(my_str)
    numbers_list.seek(0)
    list_num = numbers_list.readline().split()
    for i in list_num:
        elem_sum += int(i)
    print(f"Сумма всех чисел в файле: {elem_sum}")
