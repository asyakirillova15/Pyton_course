class Stationary:
    title = 'stationery'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    title = "Шариковая ручка"

    def draw(self):
        print(f'{self.title} рисует синюю нестираемую линию')


class Pencil(Stationary):
    title = "Простой карандаш"

    def draw(self):
        print(f'{self.title} рисует серую стираемую линию')


class Handle(Stationary):
    title = "Красный маркер"

    def draw(self):
        print(f'{self.title} рисует толстую красную линию')


thing_1 = Stationary()
thing_1.draw()
thing_2 = Pen()
thing_2.draw()
thing_3 = Pencil()
thing_3.draw()
thing_4 = Handle()
thing_4.draw()
