# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.


# БАНКОМАТ

class Terminal:
    __cash: float = 0
    __LIMIT_OPERATION = 50
    __ERROR_OPERATION = "Ошибка операции\n"
    __STEP_OPERATION = 3  # шаг операции на которой происходит насления
    __CALCULATION = 0.03  # начисление процентов за операции
    __WITHDRAWAL_PERCENTAGE = 0.015  # процент на снятие
    __LOWER_LIMIT = 30
    __UPPER_LIMIT = 600
    __RICHES = 5_000_000
    __WEALTH_TAX = 0.1  # налог на богатство
    _count = 0
    log_list = []

    # Действия клиента
    def __choice_user(self) -> int:
        print("Допустимые действия: ", "1.Пополнить.", "2.Снять.", "3.Выйти.", "4.Список операций", sep="\n")
        return int(input(">> "))

    # метод запрашивает и возвращает число, после проверки на корректность
    def __account_refill(self) -> float:
        amount = float(input(f"Введите сумму, которая кратна {self.__LIMIT_OPERATION} : >> "))
        if not amount % self.__LIMIT_OPERATION:
            return amount
        else:
            print(self.__ERROR_OPERATION)
            return 0

    # метод проверки суммы процента для снятия
    def __check_withdrawal_cash(self, amount: float) -> float:
        prc = amount * self.__WITHDRAWAL_PERCENTAGE
        return prc if self.__LOWER_LIMIT < prc < self.__UPPER_LIMIT else 0

    def start(self):
        while True:
            select = self.__choice_user()
            self._count += 1
            if self.__cash > self.__RICHES:
                percent_riches = self.__cash * self.__WEALTH_TAX
                self.log_list.append(percent_riches - percent_riches * 2)  # задание семинара
                self.__cash -= percent_riches

            elif select == 1:
                add = self.__account_refill()
                self.log_list.append(add)  # задание семинара
                self.__cash += add

                if self._count % self.__STEP_OPERATION == 0:
                    deposit_amount = self.__cash * self.__CALCULATION
                    self.log_list.append(deposit_amount)  # задание семинара
                    self.__cash += deposit_amount
                print("На счету: %.2f" % round(self.__cash, 2))

            elif select == 2:
                tmp = self.__account_refill()  # Временная переменная для проверки перед снятием ( % )

                if self.__cash < tmp:
                    print("-> Нельза снять больше чем на счету\n")
                    continue
                else:
                    withdrawal_amount = tmp - self.__check_withdrawal_cash(tmp)
                    self.__cash -= withdrawal_amount
                    self.log_list.append(withdrawal_amount - withdrawal_amount * 2)  # задание семинара
                    print("На счету: %.2f" % round(self.__cash, 2))

            elif select == 3:
                exit("-> Программа завершенна штатно")
            elif select == 4:
                print(self.log_list)  # задание семинара
            else:
                self._count += 1
                print(self.__ERROR_OPERATION)


term = Terminal()
term.start()
