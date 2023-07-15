# ✔ Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.
# ✔ *Верните все возможные варианты комплектации рюкзака.

BAG_LIMIT = 10

thing_bag = [{"Спички": 0.1, "Фонарик": 1, "Аптечка": 1, "Топор": 3, "Котелок": 1, "Еда": 2, "Кружка": 0.5},
             {"Кружка": 0.5, "Теплые вещи": 5, "Аптечка": 1, "Нож": 0.5, "Огниво": 0.5, "Палатка": 5}]


def bag_capacity(bag: list, limit: int) -> list:
    sum_weight = 0
    bags_list = []
    for bags in bag:
        for item in bags.items():
            sum_weight += item[1]
        if sum_weight <= limit:
            bags_list.append(bags)
        sum_weight = 0
    return bags_list


def print_bag(bags: list):
    if bags:
        for item in bags:
            print(f"Подходящий набор - {item}")
    else:
        print("Нет подходящих наборов")


print_bag(bag_capacity(thing_bag, BAG_LIMIT))
