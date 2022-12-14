# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5⁵ = 0 или 10*x² = 0  ""

import os
import random

simbols = "  ²³⁴⁵⁶⁷⁸⁹"

def insertNumberN(welcom_string: str):
    while True:
        try:
            n = int(input(welcom_string))
            break
        except:
            print('введите число цифрами без других символов')
    return n

def generate_list(long: int, start: int, stop: int, is_random: bool, is_real: bool):
    '''
    Создает спискок с кол-ом элементов {long},
    элементы примают случайное значение от {start} до {stop},
    при условии {is_random}.
    флаг {is_real} позволит создать список вещественных чисел.
    '''
    lst = [item for item in range(long)]
    if is_random:
         lst = [random.randint(start, stop) for item in lst]
    if is_real:
         lst = [round(item+random.random(),2) for item in lst]
    # if is_random:
    #     for a in range(long):
    #         if is_real:
    #             lst.append(round(random.randint(
    #                 start, stop) + random.random(), 2))
    #         else:
    #             lst.append(random.randint(start, stop))
    # else:
    #     random.shuffle(lst)
    return lst

def write_file(file_path: str, lines: str):
    exist = False
    if os.path.exists(file_path):
        print(f'Попытка записи в файл {file_path}...')
        exist = True
    else:
        print(f'файл {file_path}, не существует. Создание...') 
    try:
        file = open(file_path, 'w')
        try:
            file.writelines(lines)
            if exist:
                print('Файл перезаписан...')
            else:
                print('Файл создан, файл записан...')
        except:
            print('Файл создан, запись не удалась...')
        return True
    except:
        print('Ошибка создания файла')
        return False

def create_polynom(n, lst):
    result_str = ''
    result_str_py = ''
    for i in range( n ):
        if lst[i] != 0:
            if n<10:
                result_str += (f'{lst[i]}x{simbols[n-i]} + ')
            else:
                result_str += (f'{lst[i]}x**{n-i} + ')
            result_str_py += (f'{lst[i]}x**{n-i} + ')
    if lst[n] == 0:
        result_str += (f' = 0')
        result_str_py += (f' = 0')
    else:
        result_str += (f'{lst[n]} = 0')
        result_str_py += (f'{lst[n]} = 0')
    return result_str, result_str_py
# НАЧАЛО НОВОЙ ВЕРСИИ
#'''--------------------------------------------------------------------'''

def create_member(lst: list):
    if lst[1] !=0 and lst[0] != 0 and lst[1] != 1:
        return f'{lst[1]}x**{lst[0]}'
    elif lst[0] == 0:
        return f'{lst[1]}'
    elif lst[1] == 1:
        return f'x**{lst[0]}'
    return ''

def create_polynom_new(lst: list):
    result = str()
    lst = list(reversed(list(enumerate(reversed(lst)))))
    print(lst)
    result = (' + '.join(filter(lambda x: x != 0, map(create_member, lst))))
    return f'{result} = 0'

#  КОНЕЦ НОВОЙ ВЕРСИИ
#'''------------------------------------------------------------------------'''


def main(file_path_end = r'res/task4_output.txt'):
    koef_min = 0
    koef_max = 100
    os.system('cls' if os.name == 'nt' else 'clear')
    print(''' Программа принимает на вход число N,
    создает спискок от (-N до N), на основе этого списка
    создает многочлен степени N'''.replace('   ', ''))
    n = insertNumberN('Введите номер степени N: ')

    lst = generate_list(n + 1, koef_min, koef_max, True, True)
    
    print(f'Получившийся список - {lst}')
    scrpt_dir = os.path.dirname(__file__)
    file_path = os.path.join(scrpt_dir, file_path_end)
    result_str, result_str_py = create_polynom(n, lst)
    print(result_str)
    file_exist = write_file(file_path, result_str_py)
    print(create_polynom_new(lst))

if __name__ == "__main__":
    main()