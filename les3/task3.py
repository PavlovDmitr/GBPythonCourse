# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from task1 import generate_list, clear_screen, insertNumberN

def min_max_list(lst):
    min = lst[0]
    max = lst[0]
    for i in range(1, lst.__len__()):
        if lst[i] > max:
            max = lst[i]
        if lst[i] < min:
            min = lst[i]
    return(min, max)

def main():
    clear_screen()
    print(''' Программа создает список случайных 
    целых вещественных чисел и находит разницу между 
    максимальным и минимальным значением дробной части элементов''' .replace('    ', ''))
    n = insertNumberN()
    lst = generate_list(n, 1, 10, True, True)
    print(f'Оригинальный список - {lst}')
    lst_len = lst.__len__()
    result = list()
    for i in range(lst_len):
        result.append(round( lst[i] - lst[i]//1 ,2))
    (min, max) = min_max_list(result)
    print(f''' Минимальное значение дробной части - [{min}],
    Максимальное значение дробной части - [{max}],
    Разница между максимальной и минимальной - [{max-min}]'''.replace('   ', ''))

if __name__ == '__main__':
    main()