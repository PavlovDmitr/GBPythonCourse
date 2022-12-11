# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 117 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
import os, sys
import time
from random import randint as rint
from print_char import printch
from priority_start import priority_start

class player():
    name: str
    score: int
    win: bool
    auto: bool
player1 = player()
player2 = player()

def init_game(p2auto = False):
    player1.name = 'player1'
    player1.score = 0
    player1.win = False
    player1.auto = False
    player2.name = 'player2'
    player2.score = 0
    player2.win = False
    player2.auto = p2auto

def start_game():
    candy = rint(111,120)
    welcom_string = f'''ИГРА
На столе лежит {candy} конфет
Игроки поочереди берут от 1 до 28 конфет со стола
Кто из игроков заберет последнюю конфету - тот и победил'''
    printch(welcom_string)
    return candy 

def player_step(candy: int, player_dmg: int, playerN: player):
    if player_dmg > 28:
        playerN.score -= 5
        print('Вы вышли за допустимый диапозон сверх 28 конфет - штраф 5 конфет')
        return candy
    elif player_dmg < 1:
        playerN.score -= 5
        print('Вы пытаетесь обмануть игру - штраф 50 конфет')
        return candy
    candy = candy - player_dmg
    if candy > 0:
        playerN.score += player_dmg
        return candy
    else:
        playerN.score += candy
        playerN.win = True
        return 0

def try_convert_to_int(data: str):
    if data.isdigit():
        try:
            return int(data)
        except: return 'Попробуйте еще раз'
    else: return 'Попробуйте еще раз'
    
def player2_auto(): 
    str = input('Введите ДА если желаете использовать "БОТа" в качестве второго игрока ')
    if str == 'ДА':
        return True
    return False

def main():
    while True:
        init_game(player2_auto())
        os.system('cls' if os.name == 'nt' else 'clear')
        roll = priority_start()
        candy = start_game()
        n = 1
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            if roll == 1 and candy > 0:
                print(f'  {player1.name} - {player1.score} конфет собрал | {player2.name} - {player2.score} конфет собрал')
                print(f'Шаг {n}')
                player_dmg = input(f'{player1.name} введите кол-во конфет ')
                player_dmg = try_convert_to_int(player_dmg)
                if type(player_dmg) == int:
                    candy = player_step(candy, player_dmg, player1)
                    roll = 2
                    n +=1
            elif roll == 2 and candy > 0:
                print(f'  {player1.name} - {player1.score} конфет собрал | {player2.name} - {player2.score} конфет собрал')
                print(f'Шаг {n}')
                if player2.auto:
                    player_dmg = rint(1, 28)
                else: 
                    player_dmg = input(f'{player2.name} введите кол-во конфет ')
                    player_dmg = try_convert_to_int(player_dmg)
                if type(player_dmg) == int:
                    candy = player_step(candy, player_dmg, player2)
                    roll = 1
                    n +=1
            else: break
        print(f'{player1.name if player1.win else player2.name} ПОЗДРАВЛЯЕМ ВЫ ПОБЕДИЛИ!')
        exit_code = input("Введите exit для выхода, Enter для повторной игры: ")
        if exit_code == 'exit':
            break


if __name__=='__main__':
    main()
