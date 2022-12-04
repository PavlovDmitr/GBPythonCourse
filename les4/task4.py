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
    lst = list()
    if is_random:
        for a in range(long):
            if is_real:
                lst.append(round(random.randint(
                    start, stop) + random.random(), 2))
            else:
                lst.append(random.randint(start, stop))
    else:
        lst = list(a for a in range(start, stop))
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


def main(file_path_end = r'res\task4_output.txt'):
    koef_min = 0
    koef_max = 100
    print(''' Программа принимает на вход число N,
    создает спискок от (-N до N), на основе этого списка
    создает многочлен степени N'''.replace('   ', ''))
    n = insertNumberN('Введите номер степени N: ')

    lst = generate_list(n + 2, koef_min, koef_max, True, False)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'Получившийся список - {lst}')
    scrpt_dir = os.path.dirname(__file__)
    file_path = os.path.join(scrpt_dir, file_path_end)
    result_str = ''
    result_str_py = ''
    
    for i in range( n + 1):
        if n<9:
            result_str = result_str + (f'{lst[i]}x{simbols[n-i+1]} + ')
        else:
            result_str = result_str + (f'{lst[i]}x**{n-i+1} + ')
        result_str_py = result_str_py + (f'{lst[i]}x**{n-i+1} + ')
    result_str = result_str + (f'{lst[n+1]} = 0')
    result_str_py = result_str_py + (f'{lst[n+1]} = 0')
    print(result_str)
    file_exist = write_file(file_path, result_str_py)


if __name__ == "__main__":
    main()
