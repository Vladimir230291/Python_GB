# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.

from sem_10_OOP.task5_Animal import Cat


class Factory(Cat):
    def __init__(self, name: str, age: int, color: str = None):
        super().__init__(name, age, color)

    cat_1 = Cat("Барсик", 3, "Черный")


print(Factory.cat_1)
