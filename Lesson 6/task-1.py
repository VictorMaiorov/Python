import time
import itertools


class TrafficLight:
    __color = [["Красный", 2, 31], ["Желтый", 2, 33], ["Зелёный", 2, 32], ["Желтый", 2, 33]]

    def run(self):
        for el in itertools.cycle(self.__color):
            print(f"\r\033[{el[2]}m\033[1m{el[0]}", end="")
            time.sleep(el[1])


trafficlight = TrafficLight()
trafficlight.run()
