# Реализуйте алгоритм перемешивания списка.

from task4 import generate_list
from random import shuffle

def main():
    print('Введите размерность списка: ')
    n = int(input())
    lst = generate_list(n)
    print(f'изначальный список - {lst}')
    shuffle(lst)
    print(f'перемешаный список - {lst}')

if __name__=='__main__':
    main()

