# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

for i in range(2, 11):
    print()
    for j in range(2, 10):
        print(f"{j} * {i} = {i * j}\t", end="   ")
# Так я и не додумался как сделать перенос, как в школьной тетрадке
