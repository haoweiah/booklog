


# if __name__ == '__main__':
#     def main():
#         list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
#         list2 = sorted(list1)
#
#         list3 = sorted(list1, reverse=True)
#
#         list4 = sorted(list1, key=len)
#         print(list1, list2, list3, list4)
#
# main()
# import os, sys
# def gef():
#     f = [{x:y} for x in "ABCDEF" for y in "12345"]
#
#     print(f)
#     print(sys.getsizeof(f))
#     f1 = ({x:y} for x in "ABCDEF" for y in "12345")
#     print(sys.getsizeof(f1))
#
# gef()
# import time, os
# def main():
#     content = '北京欢迎你为你开天辟地…………'
#
#     while 1:
#         # os.system("clear")
#         print("\r{}".format(content), end="", flush=True)
#         time.sleep(0.5)
#         content = content[1:] + content[0]
#
# if __name__ == '__main__':
#     main()

# import random
# all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# code = ""
# for _ in range(4):
#     code += random.choice(all_chars)
#
# print(code)

from random import randrange, randint, sample

def random_select():
    """
    sui ji xuanze
    :return:
    """

    red_ball = [x for x in range(1,34)]
    selected_balls = sample(red_ball, 6)
    selected_balls.sort()
    selected_balls.append(randint(1,16))
    return selected_balls


def Christian(): # jidu tu
    persions = [True] * 30
    counter, index, number = 0,0,0
    while counter < 15:
        if persions[index]:
            number += 1
            if number == 9:
                persions[index] = False
                counter += 1
                number = 0

        index += 1
        index %= 30
    print(persions)


import os


def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('clear')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('clear')
            print_board(curr_board)
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'


if __name__ == '__main__':
    main()
