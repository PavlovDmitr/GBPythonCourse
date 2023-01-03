from sys import stdout
import os
import json
import copy
yes = ['y', 'Y', 'Yes', 'YES']
no = ['n', 'N', 'NO', 'No', 'no']
def clear_scr():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_user(data: dict) -> dict:
    result = str()
    for item in data.items():
        print(item[1])
        res = ';'.join(item[1].values())
        result = '{}{}\n'.format(result, res)
    print(result) 
    res = {'text': result }
    return res

def search_user(data: str, search_param: str) -> list:
    result = list()
    data = data.split('\n')
    for item in data:
        if item.lower().find(search_param.lower())>-1:
            print(item)
            result.append(item)
    return '\n'.join(result) if len(result) > 0 else '\n'.join(data)

def delete_user(data: list[str], delete_param: str) -> list:
    clear_scr()
    del_pass = False
    res_list = []
    for i in range(len(data)):
        if data[i].lower().find(delete_param.lower())>-1:
            print('{}, {}'.format(i, data[i]))
            res_list.append(i)
            del_pass = True
    if del_pass:
        while True:
            del_p = input('Выберите из списка объект для удаления, или введите NO(n/N/no/No) для выхода: ')
            if del_p not in no:
                try:
                    del_p = int(del_p)
                    if del_p in res_list:
                        break
                except:
                    clear_scr()
            else: return data
        print('Удаляем -', data.pop(del_p))
    else: input('Не найдены записи для удаления. Нажмите Enter для продолжения...')
    return data

def export_format(data: list[str], export_format: str) -> str:
    if export_format == 'TXT':
        newdata = str()
        for item in data:
            newdata += item.replace(';', ' ')
            newdata += '\n'
        return newdata
    
    elif export_format == 'CSV':
        return '\n'.join(data)
        
    elif export_format == 'JSON':
        new_dict = dict(dict())
        tmp = dict()
        count = 1
        for item in data:
            if len(item) > 0:
                tmp.clear()
                tmp_item = item.split(';')
                tmp["name"] = tmp_item[0]
                tmp["surname"] = tmp_item[1]
                tmp["birth"] = tmp_item[2]
                tmp["tele"] = tmp_item[3]
                new_dict[str(count)] = copy.deepcopy(tmp)
                count += 1
        return json.dumps(new_dict, indent=4, ensure_ascii=False)
    
    elif export_format == 'XML':
        count = 1
        xml = '<?xml version ="1.0" encoding="UTF-16"?>\n'
        xml += '<base>\n'
        for item in data:
            if len(item) > 0:
                tmp_item = item.split(';')
                xml += '    <count id="{}">\n'.format(count)
                xml += '        <name>{}</name>\n'.format(tmp_item[0])
                xml += '        <surname>{}</surname>\n'.format(tmp_item[1])
                xml += '        <birth>{}</birth>\n'.format(tmp_item[2])
                xml += '        <tele>{}</tele>\n'.format(tmp_item[3])  
                xml += '    </count>\n' 
                count += 1
        xml += '</base>'
        return xml

    else: return data
    

