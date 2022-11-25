# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на

# указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
import os

def read_file(file_path):
    result = list()
    print('Попытка чтения файла file.txt...')
    if os.path.exists(file_path):
        try:
            file = open(file_path, 'r')
            file_lines = file.readlines()
            for line in file_lines:
                result.append(int(line.split('\n')[0]))
        finally:
            file.close()
            if result.__len__() < 1:
                print('Файл пуст')
            return result
    else:
        print('файл отсутствует')
        return result

    


def insert_user():
    print('введите позиции элементов через запятую:')
    result = list(map(int, input().split(',')))
    return result


def generate_list(n):
    lst = list(a for a in range(-n, n+1))
    return lst


def mult(lst, pos):
    result = 1
    for element in pos:
        result = result*lst[element]
    return result


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    scrpt_dir = os.path.dirname(__file__)
    file_path = os.path.join(scrpt_dir, r'res/file.txt')
    os.path.exists(file_path)
    print(''' Программа принимает на вход число N,
    создает спискок от (-N до N), производит
    перемножение элементов на указанных позициях'''.replace('   ', ''))
    n = int(input('Пожалуйста введите число N - '))
    lst = generate_list(n)
    print(f'Получившийся список - {lst}')
    position = read_file(file_path)
    if position.__len__() < 1:
        position = insert_user()
    else:
        print('Считано...')
    print(f'Позиции необходимых элементов - {position}')
    print(mult(lst, position))


if __name__ == '__main__':
    main()
