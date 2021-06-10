class Road:
    def __init__(self, length, width, thickness):
        self._length = length
        self._width = width
        self._thickness = thickness

    def asphalt(self):
        return f"Для дороги длинной {self._length}м и шириной {self._width}м, при толщине слоя в {self._thickness}мм" \
               f" потребуется {(self._width * self._length * 25 * self._thickness) / 1000}т асфальта."


road = Road(length=int(input("Длина дороги (м): ")),
            width=int(input("Ширина дороги (м): ")),
            thickness=int(input("Толщина слоя (мм): ")))
print(road.asphalt())
