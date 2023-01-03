import file_manager
import model
import view
import os
BASE = 'base.csv'

def export_base(data: list[str], format: str, file_name = 'import'):
    if not os.path.exists('import'):
        os.mkdir('import')
    data = model.export_format(data, format)
    data = {'path': 'import/{}.{}'.format(file_name.lower(), format.lower()), 'text':data}
    file_manager.write_new_file(data)

def main():
    scrpt_dir = os.path.dirname(__file__)
    os.chdir(scrpt_dir)
    while True:
        select = view.main_window()
        if select == '1': # добавить
            data = view.add_user()
            data = model.add_user(data)
            data['path'] = BASE
            file_manager.add_t_base(data)

        elif select == '2': # найти
            search = view.search_user()
            data = file_manager.read_f_base({'path': BASE})
            data = model.search_user(data, search)
            data = view.view_search_data(data)
            if data['format'] != 'none' and data['file_name'] != 'none':
                export_base(data=data['text'].split('\n'), format=data['format'], file_name = data['file_name'])


        elif select == '3': # удалить
            data = view.delete_user()
            rbase = file_manager.read_f_base({'path': BASE})
            data = model.delete_user(rbase.split('\n'), data)
            if len(data) != len(rbase):
                data = {'path': BASE, 'text': '\n'.join(data)}
                file_manager.rewrite_base(data)

        elif select == '4': # экспортировать
            data = file_manager.read_f_base({'path': BASE})
            format = view.export_interface()
            export_base(format=format, data=data.split('\n'))

        elif select == '5':
            break