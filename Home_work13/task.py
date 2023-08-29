"""
Банкомат
"""
import exception


cash: float = 0
LIMIT_OPERATION = 50
ERROR_OPERATION = "Ошибка операции\n"
STEP_OPERATION = 3  # шаг операции на которой происходит насления
CALCULATION = 0.03  # начисление процентов за операции
WITHDRAWAL_PERCENTAGE = 0.015  # процент на снятие
LOWER_LIMIT = 30
UPPER_LIMIT = 600
RICHES = 5_000_000
WEALTH_TAX = 0.1  # налог на богатство
count = 0
log_list = []


# Действия клиента
def choice_user() -> int:
    print("Допустимые действия: ", "1.Пополнить.", "2.Снять.", "3.Выйти.", "4.Список операций", sep="\n")
    return int(input(">> "))


# метод запрашивает и возвращает число, после проверки на корректность
def account_refill() -> float:
    amount = float(input(f"Введите сумму, которая кратна {LIMIT_OPERATION} : >> "))
    if not amount % LIMIT_OPERATION:
        return amount
    else:
        print(ERROR_OPERATION)
        return 0


# метод проверки суммы процента для снятия
def check_withdrawal_cash(amount: float) -> float:
    prc = amount * WITHDRAWAL_PERCENTAGE
    return prc if LOWER_LIMIT < prc < UPPER_LIMIT else 0


while True:
    select = choice_user()
    count += 1
    if cash > RICHES:
        percent_riches = cash * WEALTH_TAX
        log_list.append(percent_riches - percent_riches * 2)  # задание семинара
        cash -= percent_riches

    elif select == 1:
        add = account_refill()
        log_list.append(add)  # задание семинара
        cash += add

        if count % STEP_OPERATION == 0:
            deposit_amount = cash * CALCULATION
            log_list.append(deposit_amount)  # задание семинара
            cash += deposit_amount
        print("На счету: %.2f" % round(cash, 2))

    elif select == 2:
        tmp = account_refill()  # Временная переменная для проверки перед снятием ( % )

        if cash < tmp:
            print("-> Нельза снять больше чем на счету\n")
            continue
        else:
            withdrawal_amount = tmp - check_withdrawal_cash(tmp)
            cash -= withdrawal_amount
            log_list.append(withdrawal_amount - withdrawal_amount * 2)  # задание семинара
            print("На счету: %.2f" % round(cash, 2))

    elif select == 3:
        exit("-> Программа завершенна штатно")
    elif select == 4:
        print(log_list)  # задание семинара
    else:
        count += 1
        print(ERROR_OPERATION)
