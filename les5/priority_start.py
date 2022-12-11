import sys, time, os
from random import randint

def priority_start():

    res1 = 0
    res2 = 0
    while True:
        for i in range(randint(5,10)):
            os.system('cls' if os.name == 'nt' else 'clear')
            print('  Розыгрыш права первого хода!\n')
            res1 = randint(1, 6)
            res2 = randint(1, 6)
            sys.stdout.write(f'   Игрок 1 -  {res1} | Игрок 2 - {res2}')
            sys.stdout.flush()
            time.sleep(0.5)
        
        print(f"\n   Результат игрока №1- {res1}")
        print(f"   Результат игрока №2- {res2}")
        if res1>res2:
            print(f"   Первый ход за игроком №1")
            return 1
            break
        elif res2>res1:
            print(f"   Первый ход за игроком №2")
            return 2
            break
        else: print(f"   Результаты игрока №1 игрока №2 совпали")

#priority_start()