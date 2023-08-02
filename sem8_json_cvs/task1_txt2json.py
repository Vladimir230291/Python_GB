# Задание №1
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json
import os

__all__ = ["txt_to_json"]
def txt_to_json(url_input: str, url_output: str) -> None:
    dict_json = {}
    url = url_output
    with open(url_input, 'r', encoding="utf-8") as file_in:
        for line in file_in:
            lst_line = line.replace("\n", "").split(' | ')
            dict_json[lst_line[0].capitalize()] = lst_line[1]
    with open(url_output, 'w', encoding="utf-8") as file_out:
        json.dump(dict_json, file_out, indent=2)


if __name__ == "__main__":
    os.chdir("..")  # что бы отрабатывал относительный путь.
    txt_to_json(r"sem7_file\result.txt", "sem8_json_cvs/result_task1.json")
