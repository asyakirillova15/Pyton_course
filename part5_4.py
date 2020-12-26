numerals = ['Один', 'Два', 'Три', 'Четыре']
counter = 0
with open('text_4.txt', 'r', encoding='utf-8') as numbers_list:
    for i in numbers_list:
        i = i.split()
        i[0] = numerals[counter]
        counter += 1
        i_new = ' '.join(i)
        print(i_new)
        with open('text_4_1.txt', 'a', encoding='utf-8') as new_list:
            new_list.writelines(i_new + '\n')
