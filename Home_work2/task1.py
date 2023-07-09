# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

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


# Действия клиента
def choiсe_user() -> int:
    print("Допустимые действия: ", "1.Пополнить.", "2.Снять.", "3.Выйти.", sep="\n")
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
    select = choiсe_user()
    count += 1
    if cash > RICHES:
        cash -= cash * WEALTH_TAX

    elif select == 1:
        cash += account_refill()
        if count % STEP_OPERATION == 0:
            cash += cash * CALCULATION
        print("На счету: %.2f" % round(cash, 2))

    elif select == 2:
        tmp = account_refill()  # Временная переменная для проверки перед снятием ( % )

        if cash < tmp:
            print("-> Нельза снять больше чем на счету\n")
            continue
        else:
            cash -= tmp - check_withdrawal_cash(tmp)
            print("На счету: %.2f" % round(cash, 2))

    elif select == 3:
        exit("-> Программа завершенна штатно")
    else:
        count += 1
        print(ERROR_OPERATION)
