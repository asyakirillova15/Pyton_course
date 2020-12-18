def is_letter(char):
    if 96 < char < 123:
        return True
    return False


def int_func(word_uni):
    for letter in word_uni:
        if is_letter(ord(letter)):
            continue
        else:
            return False
    return word_uni.title()


word = input("Введите слово: ")
print(int_func(word))

phrase = input("Введите фразу: ").split()

general_phrase = ""
for el in phrase:
    main = int_func(el)
    if main:
        general_phrase += f"{main} "

print(general_phrase)
