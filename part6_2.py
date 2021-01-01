from Validators import FloatValidator


class Road:
    def __init__(self, length, width):
        self._len = length
        self._w = width
        self.total_weight()

    def total_weight(self):
        mass = 25
        thickness = 5
        return self._len * self._w * mass * thickness / 1000


road_1 = Road(
        FloatValidator("Введите длину дороги: ").get_value(),
        FloatValidator("Введите ширину дороги: ").get_value(),
    )
print(road_1.total_weight())
