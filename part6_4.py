class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go_car(self):
        print("Машина поехала!")

    def stop_car(self):
        print("Машина остановилась")

    def turn(self, direction):
        if direction == 'right':
            print("Машина повернула направо")
        elif direction == 'left':
            print("Машина повернула налево")
        elif direction == 'revers':
            print("Машина развернулась и едет в обратном направлении")
        else:
            print("Введите верное направление(right/left/revers)")

    def show_speed(self):
        print(f"Машина едет со скоростью {self.speed} км/ч")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.show_speed()

    def show_speed(self):
        if self.speed > 60:
            print("Скорость превышена! Максимальная скорость 60 км/ч")
        else:
            print(f"Машина едет со скоростью {self.speed} км/ч")


class SportCar(Car):
    def max_speed(self):
        print("Машина разгоняется до максимальной скорости 300 км/ч")


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.show_speed()

    def show_speed(self):
        if self.speed > 40:
            print("Скорость превышена! Максимальная скорость 40 км/ч")
        else:
            print(f"Машина едет со скоростью {self.speed} км/ч")


class PoliceCar(Car):
    def police_signal(self):
        print("Полиция спешит, освободить дорогу!")


work_car_1 = WorkCar(35, "red", "car-1", False)
work_car_1.show_speed()
work_car_1.turn("left")

town_car_1 = TownCar(61, "dark_green", "toyota", False)
town_car_1.go_car()
print(town_car_1.color)
town_car_1.turn("right")

police_car_1 = PoliceCar(90, "white", "ford_1", True)
police_car_1.police_signal()
police_car_1.turn('revers')

sport_car_1 = SportCar(110, "yellow", "quick", False)
sport_car_1.max_speed()