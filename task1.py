# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# Любое действие выводит сумму денег 

def calculate_tax(amount):
    if amount > 5000000:
        return amount * 0.1
    return 0

def withdraw(amount, balance):
    if amount > balance:
        print("Ошибка: недостаточно средств на счете")
        return balance
    tax = calculate_tax(balance)
    amount_with_tax = amount + amount * 0.015
    if amount_with_tax > balance - tax:
        print("Ошибка: недостаточно средств на счете")
        return balance
    balance -= amount_with_tax
    balance -= tax
    return balance

def withdraw(amount, balance):
    tax = calculate_tax(balance)
    balance += amount
    balance -= amount * 0.03
    balance -= tax
    return balance

def atm(deposit):
    balance = 0
    num_operations = 0
    while True:
        print("Сумма на счете:", balance)
        action = input("Выберите действие (пополнить, снять, выйти): ")
        
        if action == "пополнить":
            amount = int(input("Введите сумму для пополнения: "))
            if amount % 50 != 0:
                print("Ошибка: сумма пополнения должна быть кратной 50")
                continue
            balance = deposit(amount, balance)
            num_operations += 1
        
        elif action == "снять":
            amount = int(input("Введите сумму для снятия: "))
            if amount % 50 != 0:
                print("Ошибка: сумма снятия должна быть кратной 50")
                continue
            balance = withdraw(amount, balance)
            num_operations += 1
        
        elif action == "выйти":
            break
        
        else:
            print("Ошибка: недопустимое действие")
        
        if num_operations % 3 == 0:
            balance -= balance * 0.03
    
    print("Спасибо! Ваш баланс:", balance)