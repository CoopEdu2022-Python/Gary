import os


def print_tictactoe():
    print('%3s|%3s|%3s' % (blank_tictactoe['blank0'], blank_tictactoe['blank1'], blank_tictactoe['blank2']))
    print('-----------')
    print('%3s|%3s|%3s' % (blank_tictactoe['blank3'], blank_tictactoe['blank4'], blank_tictactoe['blank5']))
    print('-----------')
    print('%3s|%3s|%3s' % (blank_tictactoe['blank6'], blank_tictactoe['blank7'], blank_tictactoe['blank8']))


def decide(a, b):
    if a == '0':
        blank_tictactoe['blank0'] = b
    elif a == '1':
        blank_tictactoe['blank1'] = b
    elif a == '2':
        blank_tictactoe['blank2'] = b
    elif a == '3':
        blank_tictactoe['blank3'] = b
    elif a == '4':
        blank_tictactoe['blank4'] = b
    elif a == '5':
        blank_tictactoe['blank5'] = b
    elif a == '6':
        blank_tictactoe['blank6'] = b
    elif a == '7':
        blank_tictactoe['blank7'] = b
    elif a == '8':
        blank_tictactoe['blank8'] = b
    else:
        print('输错了')


def judge():
    if blank_tictactoe['blank0'] == blank_tictactoe['blank1'] == blank_tictactoe['blank2'] == 'X ' or \
            blank_tictactoe['blank3'] == blank_tictactoe['blank4'] == blank_tictactoe['blank5'] == 'X ' or \
            blank_tictactoe['blank6'] == blank_tictactoe['blank7'] == blank_tictactoe['blank8'] == 'X ' or \
            blank_tictactoe['blank0'] == blank_tictactoe['blank3'] == blank_tictactoe['blank6'] == 'X ' or \
            blank_tictactoe['blank1'] == blank_tictactoe['blank4'] == blank_tictactoe['blank7'] == 'X ' or \
            blank_tictactoe['blank2'] == blank_tictactoe['blank5'] == blank_tictactoe['blank8'] == 'X ' or \
            blank_tictactoe['blank0'] == blank_tictactoe['blank4'] == blank_tictactoe['blank8'] == 'X ' or \
            blank_tictactoe['blank2'] == blank_tictactoe['blank4'] == blank_tictactoe['blank6'] == 'X ':
        print('玩家X赢了')
        return True
    elif blank_tictactoe['blank0'] == blank_tictactoe['blank1'] == blank_tictactoe['blank2'] == 'O ' or \
            blank_tictactoe['blank3'] == blank_tictactoe['blank4'] == blank_tictactoe['blank5'] == 'O ' or \
            blank_tictactoe['blank6'] == blank_tictactoe['blank7'] == blank_tictactoe['blank8'] == 'O ' or \
            blank_tictactoe['blank0'] == blank_tictactoe['blank3'] == blank_tictactoe['blank6'] == 'O ' or \
            blank_tictactoe['blank1'] == blank_tictactoe['blank4'] == blank_tictactoe['blank7'] == 'O ' or \
            blank_tictactoe['blank2'] == blank_tictactoe['blank5'] == blank_tictactoe['blank8'] == 'O ' or \
            blank_tictactoe['blank0'] == blank_tictactoe['blank4'] == blank_tictactoe['blank8'] == 'O ' or \
            blank_tictactoe['blank2'] == blank_tictactoe['blank4'] == blank_tictactoe['blank6'] == 'O ':
        print('玩家O赢了')
        return True


while True:
    print('游戏开始啦')

    blank_tictactoe = {'blank0': ' ', 'blank1': ' ', 'blank2': ' ', 'blank3': ' ', 'blank4': ' ', 'blank5': ' ',
                       'blank6': ' ', 'blank7': ' ', 'blank8': ' '}

    count_playerXO = []
    print_tictactoe()
    while True:
        os.system('cls')

        while True:
            player1 = input('玩家X请输入行数和列数的组合，如第一行第一列请输入0-8')
            if player1 not in count_playerXO:
                if len(count_playerXO) == 6:
                    a = str(count_playerXO.pop(0))
                    print('消除了', a, 'X')
                    blank_tictactoe['blank' + a] = ' '
                count_playerXO.append(player1)
                decide(player1, 'X ')
                win = judge()

                print_tictactoe()
                print(count_playerXO)
                os.system('cls')
                break

            else:
                print('已经有了')
        if win:
            os.system('cls')
            break

        while True:
            player2 = input('玩家O请输入行数和列数的组合，如第一行第一列请输入0-8')
            if not player2 in count_playerXO:
                if len(count_playerXO) == 6:
                    a = str(count_playerXO.pop(0))
                    print('消除了', a, 'O')
                    print(a)

                    blank_tictactoe['blank' + a] = ' '

                count_playerXO.append(player2)

                decide(player2, 'O ')
                win = judge()
                print_tictactoe()
                print(count_playerXO)
                os.system('cls')
                break

            else:
                print('已经有了')
        if win:
            os.system('cls')
            break
