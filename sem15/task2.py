# Задание №2
# 📌 На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# 📌 Напишите аналогичный декоратор, но внутри используйте
# модуль logging
import logging
from typing import Callable

logging.basicConfig(filename='log2.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


def logger_decorator(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        log_data = {'args': args, **kwargs, 'result': result}
        logger.info(log_data)
        return result

    return wrapper


@logger_decorator
def division(a: int, b: int) -> float:
    result = None
    try:
        result = a / b
    except ZeroDivisionError as e:
        result = float("inf")
    return result


if __name__ == '__main__':
    print(division(12, 3))
    print(division(12, 0))
