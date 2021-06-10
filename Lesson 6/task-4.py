from random import randint


class Car:
    def __init__(self, color, name, speed):
        self.speed = speed
        self.color = color
        self.name = name

    def show_speed(self):
        print(f"Текущая скорость автомобиля: {self.speed} КМ/Ч")

    def go(self):
        print(f"Автомобиль {self.name} поехал")

    def stop(self):
        print("Автомобиль остановился")

    def turn(self, direction):
        print(f'Автомобиль повернул {"налево" if direction == 0 else "направо"}')


class TownCar(Car):
    def show_speed(self):
        return f'Текущая скорость автомобиля: {self.speed} КМ/Ч' if self.speed < 60 else f'Текущая скорость автомобиля: {self.speed} КМ/Ч Превышение скорости!'


class WorkCar(Car):
    def show_speed(self):
        return f'Текущая скорость автомобиля: {self.speed} КМ/Ч' if self.speed < 40 else \
            f'Текущая скорость автомобиля: {self.speed} КМ/Ч Превышение скорости!'


class PoliceCar(Car):
    def __init__(self, color, name,
                 speed):  # is_police): я не понял как это работает и как добавить дополнительный параметр
        super().__init__(color, name, speed)  # is_police)


class SportCar(Car):
    pass


town_car = TownCar("Бежевый", "Жигули", randint(20, 80))
town_car.go()
print(town_car.show_speed())
town_car.turn(randint(0, 1))
town_car.stop()
print()

work_car = WorkCar("Синий", "Трактор", randint(10, 60))
work_car.go()
print(work_car.show_speed())
work_car.turn(randint(0, 1))
work_car.stop()
print()

sport_car = SportCar("Красный", "Феррари", randint(10, 60))
sport_car.go()

sport_car.turn(randint(0, 1))
sport_car.stop()
print()

police_car = PoliceCar("Белый", "Патриот", randint(10, 60))
police_car.go()

police_car.turn(randint(0, 1))
police_car.stop()
print()
