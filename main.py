class Person:
    max_up = 3
    _max_level = 80

    def __init__(self, name, race='unknown', speed=100):
        self.level = 1
        self.health = 100
        self.name = name
        self.race = race
        self._speed = speed

    def _check_level(self):
        return self.level < self._max_level

    def level_up(self):
        if self._check_level():
            self.level += 1
        else:
            self.level = self._max_level

    def change_level(self, other, quantity):
        self.health += quantity
        other.health -= quantity


class Hero(Person):
    def __init__(self, power, *args, **kwargs):
        self.power = power
        super().__init__(*args, **kwargs)


p1 = Hero("power", "Додо" "чудо", 120)
print(p1.power, p1.race)
