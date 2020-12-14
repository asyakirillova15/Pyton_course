main_box = []
add_product_request = True
while add_product_request:
    name_product = input("Введите название товара: ")
    price = input("Введите цену товара, руб.: ")
    number_product = input("Введите количество товара: ")
    unit = input("Введите единицы измерения товара: ")
    inner_box = ({"название": name_product, "цена": price, "количество": number_product, "ед": unit})
    main_box.append(inner_box)
    for el in enumerate(main_box, 1):
        print(el)
    add_product_request = input("Если вы хотите добавить еще товар, нажмите 1: ") == "1"

list1 = []
list2 = []
list3 = []
list4 = []
main_dict = {"название": list1, "цена": list2, "количество": list3, "ед": list4}
for el1 in main_box:
    list1.append(el1.get("название"))
    list2.append(el1.get("цена"))
    list3.append(el1.get("количество"))
    list4.append(el1.get("ед"))
print(main_dict.items())
