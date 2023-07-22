# Вспомните какие модули вы уже проходили на курсе.
# Создайте файл, в котором вы импортируете встроенные в модуль функции под псевдонимами. (3-7 строк импорта).

from random import randint as rd
from sys import getsizeof as size
from math import sqrt as sq

print(rd(1, 10))
x = [10, 11]
print(f"{size(x) = :}")
print(sq(50))
