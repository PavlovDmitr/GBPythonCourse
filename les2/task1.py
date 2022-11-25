# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = list(map(int, input('Введите вещественное число - ').split(',')))
summ = 0
for num in number:
    while num > 0:
        summ += num%10
        num = num//10
print(f'сумма цифр в числе {number[0]},{number[1]} = {summ}')

