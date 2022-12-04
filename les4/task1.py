# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
from task2 import insertNumberN

def main():
    print('Программа выводит в результате работы число ПИ с точностью D')
    d = insertNumberN('Пожалуйста введите D: ')
    res = float(str(math.pi)[:d+2])
    print(res)
    
if __name__=='__main__':
    main()
