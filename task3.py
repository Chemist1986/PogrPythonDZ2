# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

from fractions import Fraction

def calculate_fraction_operations(fraction1, fraction2):
  
    fraction1 = Fraction(fraction1)
    fraction2 = Fraction(fraction2)

   
    sum_result = fraction1 + fraction2


    product_result = fraction1 * fraction2

    return sum_result, product_result


input_fraction1 = input("Введите первую дробь (в формате a/b): ")
input_fraction2 = input("Введите вторую дробь (в формате a/b): ")

sum_result, product_result = calculate_fraction_operations(input_fraction1, input_fraction2)

print("Сумма дробей:", sum_result)
print("Произведение дробей:", product_result)


fraction1 = Fraction(input_fraction1)
fraction2 = Fraction(input_fraction2)

sum_check = fraction1 + fraction2
product_check = fraction1 * fraction2

print("Проверка с помощью модуля fractions:")
print("Сумма дробей:", sum_check)
print("Произведение дробей:", product_check)