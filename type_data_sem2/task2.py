# Создайте в переменной data список значений разных типов перечислив их через
# запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# ✔ порядковый номер начиная с единицы
# ✔ значение
# ✔ адрес в памяти
# ✔ размер в памяти
# ✔ хэш объекта
# ✔ результат проверки на целое число только если он положительный
# ✔ результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.
import sys

data = [1, 45, "text", 2.12, False, "text",-2]
check_value = ""
for i, item in enumerate(data, start=1):
    adress: int = id(item)
    size_of_item: int = sys.getsizeof(item)
    hash_of_item: int = hash(item)

    if type(item) == int:
        check_value = "Это целое число" if item > 0 else ""
    elif type(item) == str:
        check_value = "Это строка"

    print(f"Номер:{i} - значение: {item}\t Aдресс в памяти: {adress}    |   размер в памяти:{size_of_item}"
          f" | хеш объекта: {hash_of_item} - {check_value}")
