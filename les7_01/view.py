import os

yes = ['y', 'Y', 'YES', 'yes']
no = ['n', 'N', 'NO', 'No', 'no']
cancel = ['c', 'C']

def clear_scr():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_window():
    clear_scr()
    while True:
        print('''ГЛАВНОЕ МЕНЮ
    1. Добавить сотрудника
    2. Вывести карточку/и сотрудника/ов
    3. Удалить карточку сотрудника
    4. Экспорт в другой формат.
    5. Выход из программы''')
        res = input('> ')
        if res.isdigit() and int(res)>0 and int(res)<6:
            clear_scr()
            break
        else: 
            clear_scr()
            print('Выберите один из пунктов меню: \n')
    return res


def add_user():
    result = {}
    items = 1
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print('Создание карточки сотрудника')
        first_name = input('Введите Имя: ')
        second_name = input('Введите Фамилию: ')
        birth_day = input('Введите дату рождения: ')
        tel_number = input('Введите номер телефона: ')
        result[items] = {
            'first_name': first_name, 
            'second_name':second_name,
            'birth_day': birth_day,
            'tel_namber': tel_number}
        check = input('Добавить еще одну запись? y/n ')
        if check in yes:
            clear_scr()
            items += 1
        else: break
    return result


def search_user():
    clear_scr()
    print('Введите данные для поиска(фамилия/имя/номер телефона): ')
    data_search = input('>> ')
    return data_search

def delete_user():
    clear_scr()
    print('Введите данные для поиска и удаления: ')
    data_search = input('>> ')
    return data_search
    

def export_interface():
    clear_scr()
    print('''Выберите формат для экспорта: 
    1. Текстовый(TXT)
    2. Тектовый-табличный(CSV)
    3. Текстовый JSON
    4. Текстовый XML''')
    format = input('> ')
    if format == '1': format = 'TXT'
    elif format == '2': format = 'CSV'
    elif format == '3': format = 'JSON'
    elif format == '4': format = 'XML'
    else: 
        print('Выбран формат не из предложенных')
        format = 'none'
    return format

def view_search_data(data):
    clear_scr()
    print(data)
    print('Желаете экспортировать результат?(y/n)')
    res = input('> ')
    new_data = dict()
    new_data['text'] = data
    new_data['file_name'] = 'none'
    if res in yes:
        format = export_interface()
        if format != 'none':
            while True:
                clear_scr()
                file_name = input('Экспорт результата\nВведите имя файла: ')
                print('{}.{}'.format(file_name, format.lower()))
                res = input('Подтвердите выбор(y/Y) или отмените(n/N), отмена экспорта(c/C): ')
                if res in yes:
                    break
                elif res in cancel:
                    format = 'none'
                    break
        new_data['file_name'] = file_name
        new_data['format'] = format
    else: new_data['format'] = 'none'
    return new_data
