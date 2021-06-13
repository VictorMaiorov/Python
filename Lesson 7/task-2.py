from abc import ABC, abstractmethod


class Clothes(ABC):
    consumption_material = 0

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        Clothes.consumption_material += self.consumption

    @property
    def consumption(self):
        consumption = self.size / 6.5 + 0.5
        return float(f"{consumption:.02f}")

    def __str__(self):
        return f"Размер пальто: {self.size}, расход ткани: {self.consumption}."


class Costume(Clothes):
    def __init__(self, height):
        self.height = height
        Clothes.consumption_material += self.consumption

    @property
    def consumption(self):
        consumption = self.height * 2 + 0.3
        return float(f"{consumption:.02f}")

    def __str__(self):
        return f"Рост костюма: {self.height} см, расход ткани: {self.consumption}."


clothes_1 = Coat(54)
print(clothes_1)
clothes_2 = Costume(170)
print(clothes_2)
clothes_3 = Coat(48)
print(clothes_3)
clothes_4 = Costume(190)
print(clothes_4)

print(f"Всего материала потребуется: {Clothes.consumption_material}")
