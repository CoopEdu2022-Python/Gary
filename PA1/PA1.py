print('游戏开始啦')

blank_tictactoe = {'blank0': ' ', 'blank1': ' ', 'blank2': ' ', 'blank3': ' ', 'blank4': ' ', 'blank5': ' ',
                   'blank6': ' ', 'blank7': ' ', 'blank8': ' '}  # 变量作用打印整个表，并填上相应的值


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
    if blank_tictactoe['blank0'] == blank_tictactoe['blank1'] == blank_tictactoe['blank2'] == 'X' or \
            blank_tictactoe['blank3'] == blank_tictactoe['blank4'] == blank_tictactoe['blank5'] == 'X' or \
            blank_tictactoe['blank6'] == blank_tictactoe['blank7'] == blank_tictactoe['blank8'] == 'X' or \
            blank_tictactoe['blank0'] == blank_tictactoe['blank3'] == blank_tictactoe['blank6'] == 'X' or \
            blank_tictactoe['blank1'] == blank_tictactoe['blank4'] == blank_tictactoe['blank7'] == 'X' or \
            blank_tictactoe['blank2'] == blank_tictactoe['blank5'] == blank_tictactoe['blank8'] == 'X' or \
            blank_tictactoe['blank0'] == blank_tictactoe['blank4'] == blank_tictactoe['blank8'] == 'X' or \
            blank_tictactoe['blank2'] == blank_tictactoe['blank4'] == blank_tictactoe['blank6'] == 'X':
        print('X赢了')
        return True
    elif blank_tictactoe['blank0'] == blank_tictactoe['blank1'] == blank_tictactoe['blank2'] == 'O' or \
            blank_tictactoe['blank3'] == blank_tictactoe['blank4'] == blank_tictactoe['blank5'] == 'O' or \
            blank_tictactoe['blank6'] == blank_tictactoe['blank7'] == blank_tictactoe['blank8'] == 'O' or \
            blank_tictactoe['blank0'] == blank_tictactoe['blank3'] == blank_tictactoe['blank6'] == 'O' or \
            blank_tictactoe['blank1'] == blank_tictactoe['blank4'] == blank_tictactoe['blank7'] == 'O' or \
            blank_tictactoe['blank2'] == blank_tictactoe['blank5'] == blank_tictactoe['blank8'] == 'O' or \
            blank_tictactoe['blank0'] == blank_tictactoe['blank4'] == blank_tictactoe['blank8'] == 'O' or \
            blank_tictactoe['blank2'] == blank_tictactoe['blank4'] == blank_tictactoe['blank6'] == 'O':
        print('O赢了')
        return True


count_player1 = []
count_player2 = []
while True:
    player1 = input('玩家X请输入行数和列数的组合，如第一行第一列请输入0-8')
    if not player1 in count_player1 and not player1 in count_player2:
        count_player1.append(player1)
        decide(player1, 'X ')
        judge()
        print_tictactoe()
        break

    else:
        print('已经有了')

while True:
    player2 = input('玩家O请输入行数和列数的组合，如第一行第一列请输入0-8')
    if not player2 in count_player1 and not player1 in count_player2:
        count_player2.append(player2)
        decide(player2, 'O ')
        judge()
        print_tictactoe()
        break
    else:
        print('已经有了')
