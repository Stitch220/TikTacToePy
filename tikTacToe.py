        ### Tik-Tac-Toe ###
#   Author: Conner Gawlik           #
#   E-Mail: gawlik.conner@gmail.com #

import random
from random import choices

print ("Tic Tac Toe Game")

game_active = True
active_player = 'X'

field = [" ",
         "1","2","3",
         "4","5","6",
         "7","8","9"]

#print Field
def draw_field():
    print (field[1] + "|" + field[2] + "|" + field[3] )
    print (field[4] + "|" + field[5] + "|" + field[6] )
    print (field[7] + "|" + field[8] + "|" + field[9] )
draw_field()

def player_input():
    global game_active
    while True:
        turn = input("Please select a field: ")
        #end game
        if turn == 'q':
            game_active = False
            return
        try:
            turn = int(turn)
        except ValueError:
            print("Please insert a number between 1 and 9!")
        else:
            if turn >= 1 and turn <= 9:
                if field[turn] == 'X' or field[turn] == 'O':
                    print("The Field is already occupied! Choose an other")
                else:
                    return turn
            else:
                print("Number has to be between 1 and 9!")

def swap_player():
    global active_player
    if active_player == 'X':
        active_player = 'O'
    else:
        active_player = 'X'


def check_win():
    #three equal fields => this player won

    #check rows
    if field[1] == field[2] == field[3]:
        return field[1]
    if field[4] == field[5] == field[6]:
        return field[4]
    if field[7] == field[8] == field[9]:
        return field[7]
    
    #check column
    if field[1] == field[4] == field[7]:
        return field[1]
    if field[2] == field[5] == field[8]:
        return field[2]
    if field[3] == field[6] == field[9]:
        return field[3]
    
    #check diagonal
    if field[1] == field[5] == field[9]:
        return field[5]
    if field[3] == field[5] == field[9]:
        return field[5]

def check_draw():
    if (field[1] == 'X' or field[1] == 'O') \
        and (field[2] == 'X' or field[2] == 'O') \
        and (field[3] == 'X' or field[3] == 'O') \
        and (field[4] == 'X' or field[4] == 'O') \
        and (field[5] == 'X' or field[5] == 'O') \
        and (field[6] == 'X' or field[6] == 'O') \
        and (field[7] == 'X' or field[7] == 'O') \
        and (field[8] == 'X' or field[8] == 'O') \
        and (field[9] == 'X' or field[9] == 'O') :
            return ('draw')

while game_active:
    print ("Player " + active_player + "'s turn")

    field_AI = []
    for possible_fields in field:
        if possible_fields != 'X' and possible_fields != 'O' and possible_fields != ' ':
            field_AI += possible_fields

    if active_player == 'O':
        turn = int(random.choice(field_AI))
    elif active_player == 'X':
        turn = player_input()
    

    if turn:
        field[turn] = active_player
        draw_field()

        win = check_win()
        if win:
            print ("Player " + win + " wins!")
            game_active = False

        draw = check_draw()
        if draw:
            print ("Draw!")
            game_active = False

        swap_player()
