from Validators import FloatValidator, NotEmptyValidator


class Worker:
    _income = None

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_total_income(self):
        print(sum(self._income.values()))


worker_1 = Position(
        NotEmptyValidator("Введите имя сотрудника: ").get_value(),
        NotEmptyValidator("Введите фамилию сотрудника: ").get_value(),
        NotEmptyValidator("Введите должность сотрудника: ").get_value(),
        FloatValidator("Введите оклад сотрудника, руб.: ", True).get_value(),
        FloatValidator("Введите премию сотрудника, руб.: ", True).get_value()
)
worker_1.get_full_name()
worker_1.get_total_income()
