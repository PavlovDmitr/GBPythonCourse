import os

def add_t_base(data: dict):

    path = data.get('path')
    print(path)
    text = data.get('text')
    with open(path, 'a', encoding='utf-8') as file:
        file.write(text)
        

def read_f_base(data):
    path = data.get('path')
    text = str()
    try:
        with open(path, 'r', encoding='utf-8') as file:
            text = file.read()
    except:         
        with open(path, 'r', encoding='utf-16') as file:
            text = file.read()

    return text

def rewrite_base(data):
    path = data.get('path')
    text = data.get('text')
    with open(path, 'w', encoding='utf-8') as file:
        file.write(text)
    

def write_new_file(data):
    path = data.get('path')
    text = data.get('text')
    with open(path, 'w', encoding='utf-16') as file:
        file.write(text)
    

