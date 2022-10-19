import os
import time


def print_tictactoe():
    print('%3s|%3s|%3s' % (blank_tictactoe['blank0'], blank_tictactoe['blank1'], blank_tictactoe['blank2']))
    print('-----------')
    print('%3s|%3s|%3s' % (blank_tictactoe['blank3'], blank_tictactoe['blank4'], blank_tictactoe['blank5']))
    print('-----------')
    print('%3s|%3s|%3s' % (blank_tictactoe['blank6'], blank_tictactoe['blank7'], blank_tictactoe['blank8']))


def decide(a, b):
    if a == '0':
        blank_tictactoe['blank0'] = b
        return True
    elif a == '1':
        blank_tictactoe['blank1'] = b
        return True
    elif a == '2':
        blank_tictactoe['blank2'] = b
        return True
    elif a == '3':
        blank_tictactoe['blank3'] = b
        return True
    elif a == '4':
        blank_tictactoe['blank4'] = b
        return True
    elif a == '5':
        blank_tictactoe['blank5'] = b
        return True
    elif a == '6':
        blank_tictactoe['blank6'] = b
        return True
    elif a == '7':
        blank_tictactoe['blank7'] = b
        return True
    elif a == '8':
        blank_tictactoe['blank8'] = b
        return True
    else:
        print('输错了')
        return False


def judge():
    if blank_tictactoe['blank0'] == blank_tictactoe['blank1'] == blank_tictactoe['blank2'] == 'X ' or \
            blank_tictactoe['blank3'] == blank_tictactoe['blank4'] == blank_tictactoe['blank5'] == 'X ' or \
            blank_tictactoe['blank6'] == blank_tictactoe['blank7'] == blank_tictactoe['blank8'] == 'X ' or \
            blank_tictactoe['blank0'] == blank_tictactoe['blank3'] == blank_tictactoe['blank6'] == 'X ' or \
            blank_tictactoe['blank1'] == blank_tictactoe['blank4'] == blank_tictactoe['blank7'] == 'X ' or \
            blank_tictactoe['blank2'] == blank_tictactoe['blank5'] == blank_tictactoe['blank8'] == 'X ' or \
            blank_tictactoe['blank0'] == blank_tictactoe['blank4'] == blank_tictactoe['blank8'] == 'X ' or \
            blank_tictactoe['blank2'] == blank_tictactoe['blank4'] == blank_tictactoe['blank6'] == 'X ':
        print('\033[5;36;47m玩家X赢了\033[0m')
        return True
    elif blank_tictactoe['blank0'] == blank_tictactoe['blank1'] == blank_tictactoe['blank2'] == 'O ' or \
            blank_tictactoe['blank3'] == blank_tictactoe['blank4'] == blank_tictactoe['blank5'] == 'O ' or \
            blank_tictactoe['blank6'] == blank_tictactoe['blank7'] == blank_tictactoe['blank8'] == 'O ' or \
            blank_tictactoe['blank0'] == blank_tictactoe['blank3'] == blank_tictactoe['blank6'] == 'O ' or \
            blank_tictactoe['blank1'] == blank_tictactoe['blank4'] == blank_tictactoe['blank7'] == 'O ' or \
            blank_tictactoe['blank2'] == blank_tictactoe['blank5'] == blank_tictactoe['blank8'] == 'O ' or \
            blank_tictactoe['blank0'] == blank_tictactoe['blank4'] == blank_tictactoe['blank8'] == 'O ' or \
            blank_tictactoe['blank2'] == blank_tictactoe['blank4'] == blank_tictactoe['blank6'] == 'O ':
        print('\033[5;36;47m玩家O赢了\033[0m')
        return True


while True:
    print('游戏开始啦')

    blank_tictactoe = {'blank0': ' ', 'blank1': ' ', 'blank2': ' ', 'blank3': ' ', 'blank4': ' ', 'blank5': ' ',
                       'blank6': ' ', 'blank7': ' ', 'blank8': ' '}

    count_playerXO = []
    os.system('cls')
    print_tictactoe()
    while True:

        while True:
            player1 = input('玩家X请输入行数和列数的组合，如第一行第一列请输入0-8')
            if player1 == '0' or player1 == '1' or player1 == '2' or player1 == '3' or player1 == '4' or player1 == '5' \
                    or player1 == '6' or player1 == '7' or player1 == '8':

                if player1 not in count_playerXO:
                    if len(count_playerXO) >= 7:
                        a = str(count_playerXO.pop(0))
                        print('消除了', a, 'X')
                        blank_tictactoe['blank' + a] = ' '

                    if decide(player1, 'X '):
                        count_playerXO.append(player1)

                    win = judge()
                    os.system('cls')
                    print_tictactoe()

                    break

                else:
                    os.system('cls')
                    print('\033[1;31;47m已经有了\033[0m')

                    print_tictactoe()
                if win:
                    os.system('cls')
                    print_tictactoe()
                    print('\033[5;36;47m玩家X赢了\033[0m')
                    time.sleep(5)
                    break

            else:
                os.system('cls')
                print('\033[1;31;47m输错了\033[0m')
                print_tictactoe()

        if win:
            break

        while True:
            player2 = input('玩家O请输入行数和列数的组合，如第一行第一列请输入0-8')
            if player2 == '0' or player2 == '1' or player2 == '2' or player2 == '3' or player1 == '4' or player1 == '5' \
                    or player2 == '6' or player2 == '7' or player1 == '8':

                if player2 not in count_playerXO:

                    if len(count_playerXO) >= 7:
                        a = str(count_playerXO.pop(0))
                        print('消除了', a, 'O')
                        print(a)

                    if decide(player2, 'O '):
                        count_playerXO.append(player2)

                    count_playerXO.append(player2)
                    win = judge()
                    os.system('cls')
                    print_tictactoe()

                    break

                else:
                    os.system('cls')
                    print('已经有了')

                    print_tictactoe()

                if win:
                    os.system('cls')
                    print_tictactoe()
                    print('\033[5;36;47m玩家O赢了\033[0m')
                    time.sleep(5)
                    break

            else:
                os.system('cls')
                print('\033[1;31;47m输错了\033[0m')
                print_tictactoe()
        if win:
            break
