# Создайте несколько переменных разных типов.
# Проверьте к какому типу относятся созданные переменные.
a: int = 1
b: str = "str"
c: float = 1.2
d: bool = True
e: list = [0, 1, 3]
print(type(a), type(b), type(c), type(d), type(e), sep="\n")

if type(a) == int:
    print("ok")
else:
    print("not")
