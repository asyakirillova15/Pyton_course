class Store:
    main_box = []
    filial_1 = []
    filial_2 = []

    def __init__(self):
        print("\nДобрый день, приветствуем на нашем складе")
        Menu.show_main_menu()

    @classmethod
    def receipt(cls, obj):
        Store.main_box.append(obj.one_item)
        Menu.return_main_menu()

    @staticmethod
    def show_main_box():
        if not Store.main_box:
            print("\n   Пока не добавлено ни одной позиции")
        else:
            for el in enumerate(Store.main_box, 1):
                print(el)

    @staticmethod
    def show_filial_a():
        if not Store.filial_1:
            print("\n   Пока не добавлено ни одной позиции")
        else:
            for el in enumerate(Store.filial_1, 1):
                print(el)

    @staticmethod
    def show_filial_b():
        if not Store.filial_2:
            print("\n   Пока не добавлено ни одной позиции")
        else:
            for el in enumerate(Store.filial_2, 1):
                print(el)

    @staticmethod
    def transfer(fil):
        while True:
            index = input("Выберете порядковый номер позиции: ")
            index = OfficeEquipment.validator(index, "int")
            if type(index) == int:
                if 0 < index <= len(Store.main_box):
                    break
        print(index)
        ind = index - 1
        if not Store.main_box:
            print("\n   Пока не добавлено ни одной позиции. \nДобавьте позиции и их можно будет перенести\n")
        else:
            if fil == 1:
                Store.filial_1.append(Store.main_box[ind])
                del Store.main_box[ind]
            else:
                Store.filial_2.append(Store.main_box[ind])
                del Store.main_box[ind]
            print("\nДанные отправлены")


class OfficeEquipment:  # класс Оргтехника
    price = None
    quantity = None
    name = None

    def __init__(self):
        self.model = input("Введите модель товара: ")
        while True:
            self.price = input("Введите цену товара, руб.: ")
            self.price = self.validator(self.price, "float")
            if type(self.price) == float:
                break

        while True:
            self.quantity = input("Введите количество товара, шт: ")
            self.quantity = self.validator(self.quantity, "int")
            if type(self.quantity) == int:
                break

        self.one_item = (
            {"название": self.name, "модель": self.model, "цена, руб.": self.price, "количество, шт.": self.quantity}
        )
        print("\nДанные успешно добавлены!")

    @classmethod
    def validator(cls, el, valid):
        try:
            if valid == "float":
                el = float(el)
                if el > 0:
                    return el
                else:
                    raise MyOwnError("Введите положительное число")
        except ValueError:
            print("Введено некорректное число")
        except MyOwnError as err:
            print(err)
        try:
            if valid == "int":
                el = int(el)
                if el > 0:
                    return el
                else:
                    raise MyOwnError("Введите положительное число")
        except ValueError:
            print("Введено некорректное число")
        except MyOwnError as err:
            print(err)


class Printer(OfficeEquipment):
    def __init__(self):
        self.name = 'Принтер'
        super(Printer, self).__init__()

    def print(self, number):
        return f'Принтер {self.name} распечатал {number} страниц'


class Scanner(OfficeEquipment):
    def __init__(self):
        self.name = 'Сканер'
        super(Scanner, self).__init__()

    def scan(self, number):
        return f'Сканер {self.name} отсканировал {number} страниц'


class Copier(OfficeEquipment):
    def __init__(self):
        self.name = 'Копир'
        super(Copier, self).__init__()

    def copy(self, number):
        return f'Копир {self.name} скопировал {number} страниц'


class MyOwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Menu:
    @staticmethod
    def return_main_menu():
        print("-" * 50)
        user_answer = input("\n   Чтобы ввести еще один товар нажмите +\n"
                            "   Чтобы посмотреть все позиции на складе нажмите 4\n"
                            "   Для просмотра данных филиалов нажмите 6\n"
                            "   Чтобы передать технику со склада в филиал нажмите 7\n"
                            "   Для завершения 0:  ")
        Menu.convert_user_answer(user_answer)

    @staticmethod
    def transfer_menu():
        print("-" * 50)
        user_answer = input("\n   Чтобы передать технику со склада в филиал А нажмите 8\n"
                            "   Чтобы передать технику со склада в филиал B нажмите 9\n"
                            "   Для возврата в главное меню нажмите 5\n"
                            "   Для завершения 0:  ")
        Menu.convert_user_answer(user_answer)

    @staticmethod
    def show_filial_menu():
        print("-" * 50)
        user_answer = input("\n   Чтобы посмотреть данные филиала А нажмите A\n"
                            "   Чтобы посмотреть данные филиала B нажмите B\n"
                            "   Для возврата в главное меню нажмите 5\n"
                            "   Для завершения 0:  ")
        Menu.convert_user_answer(user_answer)

    @staticmethod
    def show_main_menu():
        print("-"*50)
        user_answer = input("\n   Чтобы ввести данные про новый ПРИНТЕР нажмите 1\n"
                            "   Чтобы ввести данные про новый СКАНЕР нажмите 2\n"
                            "   Чтобы ввести данные про новый КОПИР нажмите 3\n"
                            "   Для просмотра существующих позиций нажмите 4\n"
                            "   Для просмотра данных филиалов нажмите 6\n"
                            "   Для выхода нажмите 0:  ")
        Menu.convert_user_answer(user_answer)

    @staticmethod
    def convert_user_answer(user_answer):

        if user_answer == '1':
            Store.receipt(Printer())

        elif user_answer == '2':
            Store.receipt(Scanner())

        elif user_answer == '3':
            Store.receipt(Copier())

        elif user_answer == '4':
            Store.show_main_box()
            Menu.return_main_menu()

        elif user_answer == '5':
            Menu.show_main_menu()

        elif user_answer == '6':
            Menu.show_filial_menu()

        elif user_answer == '7':
            Menu.transfer_menu()

        elif user_answer == '+':
            Menu.show_main_menu()

        elif user_answer == 'A' or user_answer == 'a':
            Store.show_filial_a()
            Menu.show_filial_menu()

        elif user_answer == 'B' or user_answer == 'b':
            Store.show_filial_b()
            Menu.show_filial_menu()

        elif user_answer == '8':
            Store.transfer(1)
            Menu.show_filial_menu()

        elif user_answer == '9':
            Store.transfer(2)
            Menu.show_filial_menu()

        elif user_answer == '0':
            print("До новых встреч")
            return
        else:
            print('Некорректный ввод. Попробуйте еще раз')
            Menu.show_main_menu()


my_store = Store()
