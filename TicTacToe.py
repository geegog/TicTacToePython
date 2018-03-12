from __future__ import print_function

import os

l_r = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def tic_tac_toe(player_):

    while True:
        try:
            x = int(raw_input('Player ' + player_ + ' turn...'))
            break
        except ValueError:
            print('Please make a valid move...')

    set_position(x, player_)
    os.system('clear')

    print ('__ ' + l_r[0][0] + ' __ | __ ' + l_r[0][1] + ' __ | __ ' + l_r[0][2] + ' __')
    print ('__ ' + l_r[1][0] + ' __ | __ ' + l_r[1][1] + ' __ | __ ' + l_r[1][2] + ' __')
    print ('__ ' + l_r[2][0] + ' __ | __ ' + l_r[2][1] + ' __ | __ ' + l_r[2][2] + ' __')

    if (l_r[0][0] != ' ' and l_r[0][1] != ' ' and l_r[0][2] != ' ') and (l_r[0][0] == l_r[0][1] == l_r[0][2]):
        print ('Winner is player ' + l_r[0][0])
        return
    elif (l_r[1][0] != ' ' and l_r[1][1] != ' ' and l_r[1][2] != ' ') and (l_r[1][0] == l_r[1][1] == l_r[1][2]):
        print ('Winner is player ' + l_r[1][0])
        return
    elif (l_r[2][0] != ' ' and l_r[2][1] != ' ' and l_r[2][2] != ' ') and (l_r[2][0] == l_r[2][1] == l_r[2][2]):
        print ('Winner is player ' + l_r[2][0])
        return
    elif (l_r[0][0] != ' ' and l_r[1][0] != ' ' and l_r[2][0] != ' ') and (l_r[0][0] == l_r[1][0] == l_r[2][0]):
        print ('Winner is player ' + l_r[0][0])
        return
    elif (l_r[0][1] != ' ' and l_r[1][1] != ' ' and l_r[2][1] != ' ') and (l_r[0][1] == l_r[1][1] == l_r[2][1]):
        print ('Winner is player ' + l_r[0][1])
        return
    elif (l_r[0][2] != ' ' and l_r[1][2] != ' ' and l_r[2][2] != ' ') and (l_r[0][2] == l_r[1][2] == l_r[2][2]):
        print ('Winner is player ' + l_r[0][2])
        return
    elif (l_r[0][1] != ' ' and l_r[1][1] != ' ' and l_r[2][2] != ' ') and (l_r[0][1] == l_r[1][1] == l_r[2][2]):
        print ('Winner is player ' + l_r[0][1])
        return
    elif (l_r[0][2] != ' ' and l_r[1][1] != ' ' and l_r[2][0] != ' ') and (l_r[0][2] == l_r[1][1] == l_r[2][0]):
        print ('Winner is player ' + l_r[0][2])
        return
    elif l_r[0][0] != ' ' and l_r[0][1] != ' ' and l_r[0][2] != ' ' and l_r[1][0] != ' ' and l_r[1][1] != ' ' \
            and l_r[1][2] != ' ' and l_r[2][0] != ' ' and l_r[2][1] != ' ' and l_r[2][2] != ' ' and l_r[0][0] != ' ' \
            and l_r[1][0] != ' ' and l_r[2][0] != ' ' and l_r[0][1] != ' ' and l_r[1][1] != ' ' and l_r[2][1] != ' ' \
            and l_r[0][2] != ' ' and l_r[1][2] != ' ' and l_r[2][2] != ' ' and l_r[0][1] != ' ' and l_r[1][1] != ' ' \
            and l_r[2][2] != ' ' and l_r[0][2] != ' ' and l_r[1][1] != ' ' and l_r[2][0] != ' ' and l_r[0][2] != ' ' \
            and l_r[1][1] != ' ' and l_r[2][0] != ' ':
        print('We have a draw!!!')
        return

    if player_ == 'o':
        player_ = 'x'
    else:
        player_ = 'o'

    tic_tac_toe(player_)


def set_position(move, player):

    if move == 1 and l_r[2][0] == ' ':
        l_r[2][0] = player
    elif move == 2 and l_r[2][1] == ' ':
        l_r[2][1] = player
    elif move == 3 and l_r[2][2] == ' ':
        l_r[2][2] = player
    elif move == 4 and l_r[1][0] == ' ':
        l_r[1][0] = player
    elif move == 5 and l_r[1][1] == ' ':
        l_r[1][1] = player
    elif move == 6 and l_r[1][2] == ' ':
        l_r[1][2] = player
    elif move == 7 and l_r[0][0] == ' ':
        l_r[0][0] = player
    elif move == 8 and l_r[0][1] == ' ':
        l_r[0][1] = player
    elif move == 9 and l_r[0][2] == ' ':
        l_r[0][2] = player
    else:
        print ('Invalid Move')
        if player == 'o':
            player = 'o'
        else:
            player = 'x'
        tic_tac_toe(player)


tic_tac_toe('o')
print ('End')
