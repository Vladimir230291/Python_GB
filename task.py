class UserException(Exception):
    pass


class UserNameError(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Имя должно быть большое 6 символов"


class UserAgeError(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'возраст должен быть целым' \
               f'у Вас тип {type(self.value)} и значение {self.value}'


class User:
    MIN = 6
    MAX = 30

    def __init__(self, name, age):
        if self.MIN < len(name) <= self.MAX:
            self.name = name
        else:
            raise UserNameError(name)
        if not isinstance(age, (int, float)) or age < 0:
            raise UserAgeError(age)
        else:
            self.age = age


u = User("qwerter", -12)
print(u)
