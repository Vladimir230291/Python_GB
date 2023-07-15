# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

some_list = [1, 2, 3, 4, 1, 2, 3, 5]
result_list = []

for val in some_list:
    if some_list.count(val) > 1 and val not in result_list:
        result_list.append(val)
print(f"Повторяющиеся элементы = {result_list}")

