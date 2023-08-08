# Задание №5
# 📌 Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# 📌 У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# 📌 Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

__all__ = ["Cat", "Dog", "Fish"]


class Animal:
    def __init__(self, name: str, age: int, color: str):
        self.name = name
        self.age = age
        self.color = color

    def sleep(self):
        return "animal-sleep"

    def eat(self):
        return "animal-eat"


class Cat(Animal):

    def __init__(self, name: str, age: int, color: str = None):
        super().__init__(name, age, color)

    def say(self):
        return f"{self.name} мяукает!"

    def __str__(self):
        return f"Это кот по кличке {self.name}, его возраст {self.age} год(а), цвет у него {self.color}"


class Dog(Animal):
    def __init__(self, name: str, age: int, color: str = None):
        super().__init__(name, age, color)

    def say(self):
        return f"{self.name} гавкает"

    def __str__(self):
        return f"Это собака по кличке {self.name}"


class Fish(Animal):
    def __init__(self, name: str, age: int, color: str = None):
        super().__init__(name, age, color)

    def say(self):
        return f"Это рыба она не может издавать звуки"

    def sail(self):
        return f"Pыба по кличке {self.name} поплыла!"


if __name__ == "__main__":
    cat1 = Cat("Барсик", 2, "черный")
    dog1 = Dog("Барбос", 1, "Рыжый")
    fish = Fish("Nemo", 1, "Red-white")
    print(cat1.say(), "|", cat1.eat(), "<--cat")
    print(dog1.say(), "|", dog1.eat(), "<--dog")
    print(fish.say(), "\n" + fish.sail(), "|", fish.eat(), "<--fish")
