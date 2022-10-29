import os
import time


def print_tictactoe():  #打印空的游戏图
    print('%3s|%3s|%3s' % (blank_tictactoe['blank0'], blank_tictactoe['blank1'], blank_tictactoe['blank2']))
    print('-----------')
    print('%3s|%3s|%3s' % (blank_tictactoe['blank3'], blank_tictactoe['blank4'], blank_tictactoe['blank5']))
    print('-----------')
    print('%3s|%3s|%3s' % (blank_tictactoe['blank6'], blank_tictactoe['blank7'], blank_tictactoe['blank8']))


def decide(a, b):  #把玩家输入的数字转换成字典的键，最后打印出来
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
        print('输错了4')
        return False


def judge(): #判断输赢
    if blank_tictactoe['blank0'] == blank_tictactoe['blank1'] == blank_tictactoe['blank2'] == 'X ' or \
            blank_tictactoe['blank3'] == blank_tictactoe['blank4'] == blank_tictactoe['blank5'] == 'X ' or \
            blank_tictactoe['blank6'] == blank_tictactoe['blank7'] == blank_tictactoe['blank8'] == 'X ' or \
            blank_tictactoe['blank0'] == blank_tictactoe['blank3'] == blank_tictactoe['blank6'] == 'X ' or \
            blank_tictactoe['blank1'] == blank_tictactoe['blank4'] == blank_tictactoe['blank7'] == 'X ' or \
            blank_tictactoe['blank2'] == blank_tictactoe['blank5'] == blank_tictactoe['blank8'] == 'X ' or \
            blank_tictactoe['blank0'] == blank_tictactoe['blank4'] == blank_tictactoe['blank8'] == 'X ' or \
            blank_tictactoe['blank2'] == blank_tictactoe['blank4'] == blank_tictactoe['blank6'] == 'X ':
        print('\033[5;36;47m玩家X赢了，游戏结束\033[0m')
        time.sleep(5)
        return True
    elif blank_tictactoe['blank0'] == blank_tictactoe['blank1'] == blank_tictactoe['blank2'] == 'O ' or \
            blank_tictactoe['blank3'] == blank_tictactoe['blank4'] == blank_tictactoe['blank5'] == 'O ' or \
            blank_tictactoe['blank6'] == blank_tictactoe['blank7'] == blank_tictactoe['blank8'] == 'O ' or \
            blank_tictactoe['blank0'] == blank_tictactoe['blank3'] == blank_tictactoe['blank6'] == 'O ' or \
            blank_tictactoe['blank1'] == blank_tictactoe['blank4'] == blank_tictactoe['blank7'] == 'O ' or \
            blank_tictactoe['blank2'] == blank_tictactoe['blank5'] == blank_tictactoe['blank8'] == 'O ' or \
            blank_tictactoe['blank0'] == blank_tictactoe['blank4'] == blank_tictactoe['blank8'] == 'O ' or \
            blank_tictactoe['blank2'] == blank_tictactoe['blank4'] == blank_tictactoe['blank6'] == 'O ':
        print('\033[5;36;47m玩家O赢了，游戏结束\033[0m')
        time.sleep(5)
        return True


while True:
    print('游戏开始啦')

    blank_tictactoe = {'blank0': '0 ', 'blank1': '1 ', 'blank2': '2 ', 'blank3': '3 ', 'blank4': '4 ', 'blank5': '5 ',
                       'blank6': '6 ', 'blank7': '7 ', 'blank8': '8 '}  #一个列表，用来存放空的游戏图

    count_playerXO = [] #一个列表记录所有的棋子的位置
    os.system('cls')
    print_tictactoe()
    chose_mode = input('请选择模式(1)普通玩法 (2)进阶玩法')
    if chose_mode not in ['1', '2']: #判断玩家的输入有没有错误
        print('输错了90')
        time.sleep(5)
        continue
    win=bool()
    while True:


        while True:
            player1 = input('玩家X请输入行数和列数的组合，如第一行第一列请输入0-8')
            if player1 in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
                os.system('cls')
                if player1 not in count_playerXO: #判断玩家输入的棋的位置是否已经有了棋子
                    if chose_mode == '1':
                        if len(count_playerXO) > 8:
                            if not judge():
                                print('平局')
                                time.sleep(5)
                                break
                    elif chose_mode == '2':

                        if len(count_playerXO) > 5:
                            a = str(count_playerXO.pop(0))
                            if not judge():
                                print('消除了', a, 'X')
                                time.sleep(5)
                            blank_tictactoe['blank' + a] = ' '
                    else:
                        print('输入模式错误')
                        continue

                    if decide(player1, 'X '):
                        count_playerXO.append(player1)

                    win = judge()

                    print_tictactoe()

                    break

                else:
                    os.system('cls')
                    print('\033[1;31;47m已经有了3\033[0m')

                    print_tictactoe()

                if win:
                    os.system('cls')
                    print_tictactoe()
                    print('\033[5;36;47m玩家X赢了，游戏结束\033[0m')
                    time.sleep(5)
                    break

            else:
                os.system('cls')
                print('\033[1;31;47m输错了2\033[0m')
                print_tictactoe()

        if win:
            print('\033[5;36;47m玩家X赢了，游戏结束\033[0m')
            time.sleep(5)
            break

        while True:
            player2 = input('玩家O请输入行数和列数的组合，如第一行第一列请输入0-8')
            if player2 in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:

                if player2 not in count_playerXO:
                    os.system('cls')
                    if chose_mode == '1':
                        if len(count_playerXO) > 8:
                            if not judge():
                                print('平局')
                                break
                    elif chose_mode == '2':

                        if len(count_playerXO) > 5:
                            a = str(count_playerXO.pop(0))
                            if not judge():
                                print('消除了', a, 'O')
                                time.sleep(5)
                            blank_tictactoe['blank' + a] = ' '
                    else:
                        print('输入模式错误')
                        continue

                    if decide(player2, 'O '):
                        count_playerXO.append(player2)

                    win = judge()

                    print_tictactoe()

                    break

                else:
                    os.system('cls')
                    print('已经有了9')

                    print_tictactoe()

                if win:
                    os.system('cls')
                    print_tictactoe()
                    print('\033[5;36;47m玩家O赢了，游戏结束\033[0m')
                    time.sleep(5)
                    break

            else:
                os.system('cls')
                print('\033[1;31;47m输错了1\033[0m')

                print_tictactoe()
                time.sleep(5)
        if win:
            print('\033[5;36;47m玩家O赢了,游戏结束\033[0m')
            time.sleep(5)
            break
