#  Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многоч
import os

INPUTPATH1 = r'res/task5_input1.txt'
INPUTPATH2 = r'res/task5_input2.txt'
OUTPUTPATH = r'res/task5_output.txt'

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    scrpt_dir = os.path.dirname(__file__)
    file_path = os.path.join(scrpt_dir, INPUTPATH1)
    with open(file_path, 'r') as file1:
        text1 = file1.readline()
    file_path = os.path.join(scrpt_dir, INPUTPATH2)
    with open(file_path, 'r') as file2:
        text2 = file2.readline()
    if len(text1) > len(text2):
        max = text1
    else: max = text2
    text1 = text1.replace(' ', '').split('+')
    print(text1)
    text2 = text2.replace(' ', '').split('+')
    print(text2)
    res = list(zip(text1, text2))
    res_out = ''
    for item in res:
        res = 0
        for item2 in item:
            if not(item2.isdigit()):
                n1, n2 = item2.split('x')
            else:
                n1 = item2
                n2 = ''
            res = res + int(n1)
        if len(n2)>0:
            res = str(res)+'x'+str(n2)+' + '
        res_out = res_out + str(res)
    print(res_out)
    file_path = os.path.join(scrpt_dir, OUTPUTPATH)
    with open(file_path, 'w') as file_exist:
        file_exist.write(res_out)

if __name__=='__main__':
    main()

