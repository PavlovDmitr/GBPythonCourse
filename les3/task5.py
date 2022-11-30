# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

from task1 import clear_screen

def fibonacci(n):
    fib1 = 0
    fib2 = 1
    i = 0
    while i < n - 1:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    return(fib2)

def fib_revers(n):
    if n<0:
        return int((-1)**(n+1)*fibonacci(abs(n)))
    elif n == 0:
        return 0
    else: return fibonacci(n)
    
def main():
    print('''Программа составляет список чисел Фибоначчи влючая отрицательные индексы''')
    n = int(input("Номер элемента ряда Фибоначчи: "))
    lst_result = list()
    for i in range(-n, n+1):
        lst_result.append(fib_revers(i))
    print(lst_result)

if __name__=='__main__':
    main()