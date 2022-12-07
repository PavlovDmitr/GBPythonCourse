#  Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многоч
import os
import task4


INPUTPATH1 = r'res/task5_input1.txt'
INPUTPATH2 = r'res/task5_input2.txt'
OUTPUTPATH = r'res/task5_output.txt'

def read_poly_from_file(file_path: str):
    with open(file_path, 'r') as file1:
        polynom1 = file1.readline().split('=')[0]
    return polynom1


def open_file_write(file_path: str, res_out: str):
    with open(file_path, 'w') as file_exist:
        file_exist.write(res_out)

def compare_polynoms(polynom1: str, polynom2: str):
    result = ''
    poly1_list = polynom1.replace(' ', '').split('+') #  13x**6 + 31x**5 + 32x**4 + 3x**3 + 36x**2 + 99x**1 + 12
    poly2_list = polynom2.replace(' ', '').split('+') #  16x**6 + 95x**5 + 21x**4 + 44x**3 + 25x**2 + 39x**1 + 67
    poly_fin_list = list()
    if len(poly1_list) > len(poly2_list):
        for i in range(len(poly1_list)-len(poly2_list)):
            poly_fin_list.append(poly1_list[i])
    elif len(poly1_list) < len(poly2_list):
        for i in range(len(poly2_list)-len(poly1_list)):
            poly_fin_list.append(poly2_list[i])
    for i in poly1_list:
        for j in poly2_list:
            if (i.find('x**') >-1) and (j.find('x**')>-1):
                if (i.split('x**')[1] == j.split('x**')[1]):
                    poly_fin_list.append(str(int(i.split('x**')[0]) + int(j.split('x**')[0]))+'x**'+i.split('x**')[1])
            elif i.isdigit() and j.isdigit():
                poly_fin_list.append(str(int(i) + int(j)))
    result= ' + '.join(poly_fin_list)
    return result

def sum_polynoms(polynom1, polynom2):
    
    print(polynom1)
    
    print(polynom2)
    if len(polynom1) > len(polynom2):
        polynom1, polynom2 = polynom2, polynom1
    compare_membrs_polynom = list(zip(polynom1, polynom2))
    print(compare_membrs_polynom)
    res_out = ''
    for item in compare_membrs_polynom:
        res = 0
        for item2 in item:
            if not(item2.isdigit()):
                n1, n2 = item2.split('x')
            else:
                n1 = item2
                n2 = ''
            res += int(n1)
        if len(n2)>0:
            res = str(res)+'x'+str(n2)+' + '
        res_out += str(res)
    print(res_out)
    return res_out

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    scrpt_dir = os.path.dirname(__file__)
    task4.main(INPUTPATH1)
    task4.main(INPUTPATH2)
    file_path = os.path.join(scrpt_dir, INPUTPATH1)
    polynom1 = read_poly_from_file(file_path).split('=')[0]
    file_path = os.path.join(scrpt_dir, INPUTPATH2)
    polynom2 = read_poly_from_file(file_path).split('=')[0]
    res_out = compare_polynoms(polynom1, polynom2)
    file_path = os.path.join(scrpt_dir, OUTPUTPATH)
    open_file_write(file_path, res_out)

if __name__=='__main__':
    main()

