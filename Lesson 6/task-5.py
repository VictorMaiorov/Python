class Stationery:
    def __init__(self, title="Инструмент"):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки. {self.title}.")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки. {self.title} ручка.")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки. {self.title} карандаш.")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки. {self.title} маркер.")


stationery = Stationery()
stationery.draw()
pen = Pen("Любая")
pen.draw()
pencil = Pencil("Любой")
pencil.draw()
handle = Handle("Любой")
handle.draw()
