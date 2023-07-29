# Задание №7
# ✔️ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔️ Каждая группа включает файлы с несколькими расширениями.
# ✔️ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
__all__ = ["sort_files_by_category"]
import os
import shutil


def sort_files_by_category(source_dir):
    # Создаем словарь, где ключи - категории файлов, значения - списки расширений
    categories = {
        "Видео": [".mp4", ".avi", ".mkv"],
        "Изображения": [".jpg", ".jpeg", ".png", ".gif"],
        "Текст": [".txt", ".doc", ".pdf"],
    }

    # Создаем директории для каждой категории, если они не существуют
    for category in categories:
        category_dir = os.path.join(source_dir, category)
        os.makedirs(category_dir, exist_ok=True)

    # Получаем список всех файлов в исходной директории
    files = os.listdir(source_dir)

    for file in files:
        file_extension = os.path.splitext(file)[1]  # Получаем расширение файла

        for category, extensions in categories.items():
            if file_extension in extensions:
                source_path = os.path.join(source_dir, file)
                destination_directory = os.path.join(source_dir, category)
                destination_path = os.path.join(destination_directory, file)
                shutil.move(source_path, destination_path)
                break

if __name__ == "__main__":
    sort_files_by_category("/home/user/PycharmProjects/Python_GB/sem7_file/file_for_task4")
