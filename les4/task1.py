# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
from task2 import insertNumberN

def main():
    print('Программа выводит в результате работы число ПИ с точностью D')
    d = input('Пожалуйста введите маску D: ')
    d = len(d[d.find('.')::])
    res = float(str(math.pi)[:d+1])
    print(res)
    
if __name__=='__main__':
    main()
