# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N


def insertNumberN(welcom_string: str):
    while True:
        try:
            n = int(input(welcom_string))
            break
        except:
            print('введите число цифрами без других символов')
    return n

def main():
    print('''Программа состовляет список простых множителей числа N''')
    n = insertNumberN('Введите число N: ')
    result = []
    i = 2
    while n > 1:
        if n%i == 0:
            if result.count(i) < 1:
                result.append(i)
            n = n/i
        else: 
            i = i + 1
    print(f'список простых множетелей - {result}')
            

if __name__ == '__main__':
    main()