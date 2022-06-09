#2. Вы когда-нибудь играли в игру "Крестики-нолики"? 
# Попробуйте создать её, причем чтобы сыграть в нее можно было в одиночку.

from random import randint


game_board = [i for i in range(1, 10)] # игровое поле
prizer = 0
count_step = 0
priz_comb = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]

def print_game_board (game_board): #вывод поля на экран

    for i in range(0,7,3):
        print("|-----|-----|-----|")
        print(f"|  {game_board[i]}  |  {game_board[i+1]}  |  {game_board[i+2]}  |")
    print("|-----|-----|-----|")

def check_finish(game_b): # проверка финиша
 
    for var in priz_comb:
        if game_b[var[0]-1] == game_b[var[1]-1] == game_b[var[2]-1] == "X":
            return  -1
            
        elif game_b[var[0]-1] == game_b[var[1]-1] == game_b[var[2]-1] == "O":
            return 1

    if count_step == 9:
        return -2
        
    return 0

def check_input(tmp_step): # ввод хода и его проверка (проверяет не занята ли клетка и есть ли такая клетка.)
    
    if (tmp_step > 0) and (tmp_step < 10):
        if (game_board[tmp_step-1] != "X")and ((game_board[tmp_step-1] != "O")):
            return True
        
    return False

def step_zero():
    step_zero = randint(1,10)
    while check_input(step_zero) == False:
        step_zero = randint(1,10)
    return step_zero

def check_out ():

    if prizer == -1:
        print("\033[31m{}\033[0m".format("Крестики выиграли"))
        print_game_board (game_board)
        
    elif prizer == 1:
        print("\033[31m{}\033[0m".format("Нолики выиграли"))
        print_game_board (game_board)

    elif prizer == -2:
        print("\033[31m{}\033[0m".format("Ничья"))
        print_game_board (game_board)
        

print_game_board (game_board) # вывод доски

while prizer == 0: # играем пока не финиш

    step = int(input("\033[31m{}\033[0m".format("делайте ход. укажите номер клетки: ")))
    while check_input(step) == False: # проверка на валидность
        step = int(input("\033[31m{}\033[0m".format("делайте ход. укажите номер клетки: ")))

    game_board[step-1] = "X"
    count_step += 1
    
    print_game_board (game_board) # напечатали доску

    prizer = check_finish(game_board)
    if prizer !=0 :
        check_out ()
        break

    game_board[step_zero()-1] = "O" # сделали ход ноликом
    count_step += 1
    print("\033[31m{}\033[0m".format("Ход компьютера:"))   
    print_game_board (game_board)

    prizer = check_finish(game_board)
    if prizer !=0 :
        check_out ()
        break

