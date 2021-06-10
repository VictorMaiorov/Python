class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_profit(self):
        return f"{sum(self._income.values())}"


staff = Position("Василий", "Пупкин", "Инженер", 30000, 10000)
print(f"Работник, {staff.get_full_name()} находится на должности {staff.position} "
      f"и имеет доход с учетом премии: {staff.get_full_profit()}")
