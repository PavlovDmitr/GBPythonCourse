# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from task1 import generate_list, clear_screen, insertNumberN

def main():
    clear_screen()
    print(''' Программа создает список случайных 
    целых чисел и вычисляет произведение пар
    (1, n), (2, n-1), (3, n-2)...элементов этого списка''' .replace('    ', ''))
    n = insertNumberN()
    lst = generate_list(n, 1, 10, True, False)
    print(f'Оригинальный список - {lst}')
    lst_len = lst.__len__()
    result = list()
    for i in range(lst_len//2):
        result.append(lst[i]*lst[lst_len-i-1])
    if lst_len%2 != 0:
        print('''Кол-во элементов списка нечетное
        центральный элемент умножен сам на себя'''.replace('    ', ''))
        result.append((lst[(lst_len//2)])**2)
    print(f'Список произведения пар - {result}')

if __name__ == '__main__':
    main()