# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров

import logging
import argparse

logging.basicConfig(filename='log.log', encoding='utf-8', level=logging.INFO, format='%(asctime)s: %(message)s')
logger = logging.getLogger(__name__)


# функция запрашивает числовые данные от пользователя до тех пор, пока он не введёт целое или вещественное число
def get_num(text: str = None):
    while True:
        num = input(text)
        try:
            data = int(num)
            logger.info(f"{num} - целое число")
            break
        except ValueError as e:
            logger.error(f"{num} - не удалось привести к целому числу")
            try:
                data = float(num)
                logger.info(f"{num} - вещественное число")
                break
            except ValueError as e:
                logger.error(f"{num} - Не удалось привести к вещественному числу")
    return type(data)


def parse_args():
    parser = argparse.ArgumentParser(prog="get_num",
                                     description="get num from user")
    parser.add_argument('-num', '--number',
                        default='1',
                        help='Преобразует число',
                        type=get_num)
    return parser.parse_args()


if __name__ == '__main__':
    print(get_num("enter: "))
