import os

def print_base(data):
    if type(data) == list or type(data) == tuple or type(data) == dict:
        for item in data:
            print('[ {} ]'.format(item.replace('\n', '')))
    else: print('[ {} ]'.format(data.replace('\n', '')))

def main_screen_view():
    '''1. Добавление записей.
        2. Поиск записей или вывод всех записей.
        3. Удаление записей.
        4. Выход из программы'''
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print('''Программа для работы с телефонным сравочником
        доступный функционал:
        1. Добавление записей.
        2. Поиск записей или вывод всех записей.
        3. Удаление записей.
        4. Импорт в текстовом формате
        5. Выход из программы
        Выберите один из пунктов: '''.replace('    ', ' '))
        lst = ['1', '2', '3', '4', '5']
        choice = input("> ")
        if lst.count(choice) == 1:
            return choice
        else:
            os.system('cls' if os.name == 'nt' else 'clear') 
            print("Выберите один из предложеных пунктов: ")
            

def insert_data_base_view():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Пожалуйста введите данные для сохраниния в базу данных(или 3 раза нет для выхода):")
    second_name = input("Введите Фамилию: ")
    first_name = input("Введите Имя: ")
    # middlename = input("Введите Фамилию: ")
    tel_number = input("Введите номер телефона: ")
    return second_name, first_name, tel_number

def search_data_base_view():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''Введите условие поиска(фамилия/имя/телефон),
    или оставть пустым для вывода всей базы данных'''.replace('    ', ' '))
    return input("> ")

def del_data_base_view():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''Введите условие для поиска(фамилия/имя/телефон)
    и удаления найденных данных'''.replace('    ', ' '))
    return input("> ")