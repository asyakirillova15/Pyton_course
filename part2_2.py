my_list = [1, input("Введите несколько значений через пробел: ")]
var = my_list[1].split()
my_list.remove(1)
count = 0
for el in var:

    if count % 2 != 0:
        var[count - 1], var[count] = var[count], var[count - 1]
    count += 1
print(var)
