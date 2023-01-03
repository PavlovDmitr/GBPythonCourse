from datetime import datetime as dt
from time import time
import os
from view import print_base as print

def write_to_file(data, mode = 'a', base_name = r'.\base\base.csv'):
    scrpt_dir = os.path.dirname(__file__)
    base_name = os.path.join(scrpt_dir, base_name)
    if base_name.split("\\")[-1].split('.')[-1] == 'csv':
        separator = ';'
    else: separator = ' '
    try:
        with open(base_name, mode, encoding="utf-8") as file:
            for line in data:
                file.write(f"{separator.join(line.split())}\n")  
            #file.write("\n")   #"{}'\n'".format(';'.join(items))
            return True
    except:
        with open(base_name, 'w',encoding="utf-8") as file:
            for line in data:
                file.write(f"{separator.join(line.split())}\n")   
            #file.write("\n")
            return True
    
   

def read_from_file(base_name = r'.\base\base.csv'):
    scrpt_dir = os.path.dirname(__file__)
    base_name = os.path.join(scrpt_dir, base_name)
    try:
        with open(base_name, 'r',encoding="utf-8") as file:
            lines = file.readlines()
        return lines
    except: return (list('База не существует',))



def write_log(data, base_name = r'.\base\log.txt'):
    scrpt_dir = os.path.dirname(__file__)
    base_name = os.path.join(scrpt_dir, base_name)
    time = dt.now().strftime('%H:%M:%S')
    with open(base_name, 'a',encoding="utf-8") as file:
        file.write('\n{}: {}'.format(time, data))