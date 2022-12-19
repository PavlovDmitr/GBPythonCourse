from view import *
from file_menager import *
from view import print_base as print

def search_f_base(data_search):
    data = read_from_file()
    data_return = list()
    if len(data_search) > 0:
        print('Ищем [ {} ]...'.format(data_search))
        f = False
        for line in data:
            if line.find(';'.join(data_search)) > -1:
                data_return.append(line.replace('\n', '').split(';'))
                f = True
        if not f:
            return('Совпадений не найдено')
    else: data_return

def del_data_in_file(data: str):
    f = False
    file_lines = read_from_file()
    lines = search_f_base(data)
    k = input('''Подтвердите удаление(Y/y) или
    откажитесь и создайте запрос заново: '''.replace('    ', ' '))
    if k == 'y' or k == 'Y':
        for line in lines:
            if line.find(data)>-1:
                file_lines.remove(line)
                print(line)
                f = True
        write_to_file('\n'.join(file_lines), mode='w')
    if f:
        return True

def button_click():
    while True:
        choice = main_screen_view()
        if choice == '1': #Добавление записей.
            while True:
                data = insert_data_base_view()
                if data[0] != 'нет' and data[1] != 'нет' and data[2] != 'нет':
                    write_to_file(';'.join(data))
                    write_log('Добавлена запись')
                else: break
        elif choice == '2':
            data_search = search_data_base_view().split()
            search_f_base(data_search)
            input()
            write_log('Поиск по базе')
        elif choice == '3':
            data_search = del_data_base_view()
            if del_data_in_file(data_search):
                print("Удаление произведено")
                write_log('Удаление из базы')
            else:   
                print('Совпадений не найдено')
            input()
        elif choice == '4':
            break

