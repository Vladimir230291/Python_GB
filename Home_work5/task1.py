# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла

def path_absolut(text: str):
    tmp_list = text.split("/")

    res = (text, tmp_list[-1], tmp_list[-1].split(".")[-1])
    return res


print(path_absolut("/home/users/PycharmProjects/Python_GB/sem5_gen_inter.txt"))
