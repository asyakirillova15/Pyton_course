def int_func(word_uni):
    for el in word_uni:
        number_uni = ord(el)
        if number_uni in list_unicod:
            continue

        else:
            return
    return word_uni.title()


word = input("Введите слово: ")
list_unicod = list(range(97, 123))
print(int_func(word))


phrase = input("Введите фразу: ").split()
for el in phrase:
    list_word = []
    list_word.append(int_func(el))

    list_word. extend(el)
    print(list_word)
my_str = list_word.join(" ")
print(my_str)
