# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
from os import system, name

def clear_screen():
    system('cls' if name == 'nt' else 'clear')

def generate_list(long, start, stop:int, is_random, is_real:bool):
    lst = list()
    if is_random:
        for a in range(long):
            if is_real:
                lst.append(round(random.randint(start, stop)+random.random(),2))
            else: lst.append(random.randint(start, stop))
    else:
        lst = list(a for a in range(start, stop))
    return lst

def insertNumberN():
    while True:
        try:
            n = int(input('Введите кол-во элементов списка - '))
            break
        except:
            print('введите число цифрами без других символов')
    return n

def main():
    clear_screen()
    min_value = 1
    max_value = 10
    print(''' Программа создает список случайных 
    целых чисел и вычисляет сумму элементов 
    этого списка, стоящих на нечетных позициях '''.replace('    ', ''))
    n = insertNumberN()
    lst = generate_list(n, min_value, max_value, True, False)
    print(lst)
    sum=0
    for i in range(1,lst.__len__(),2):
        sum += lst[i]
    print(f'Сумма элементов на нечетных позициях - {sum}')

if __name__ == '__main__':
    main()

