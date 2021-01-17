from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def textile_calculation(self):
        pass

    def __add__(self, other):
        return self.textile_calculation + other.textile_calculation


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def textile_calculation(self):
        return round(self.size / 6.5 + 0.5)


class Costume(Clothes):
    def __init__(self, growth):
        self.growth = growth

    @property
    def textile_calculation(self):
        return round(2 * self.growth + 0.3)


coat_autumn = Coat(50)
print(coat_autumn.textile_calculation)

costume_wedding = Costume(1.65)
print(costume_wedding.textile_calculation)

print(coat_autumn + costume_wedding)
