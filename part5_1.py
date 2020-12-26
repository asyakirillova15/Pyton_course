with open('text.txt', 'w', encoding='utf-8') as new_file:
    while True:
        line_ = input("Ввод: ")
        if line_ == '':
            break
        else:
            new_file.writelines(line_ + '\n')
