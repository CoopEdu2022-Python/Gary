import os
import time


def print_tictactoe():  # 打印空的游戏图
    print('%3s|%3s|%3s' % (blank_tictactoe['blank0'], blank_tictactoe['blank1'], blank_tictactoe['blank2']))
    print('-----------')
    print('%3s|%3s|%3s' % (blank_tictactoe['blank3'], blank_tictactoe['blank4'], blank_tictactoe['blank5']))
    print('-----------')
    print('%3s|%3s|%3s' % (blank_tictactoe['blank6'], blank_tictactoe['blank7'], blank_tictactoe['blank8']))


def decide(XorO_input, X_O):  # 把玩家输入的数字转换成字典的键，最后打印出来
    if XorO_input in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
        blank_tictactoe['blank' + XorO_input] = X_O
        return True
    else:
        print('输错了4')
        return False


def judge(X_O):  # 判断输赢
    if blank_tictactoe['blank0'] == blank_tictactoe['blank1'] == blank_tictactoe['blank2'] == X_O + ' ' or \
            blank_tictactoe['blank3'] == blank_tictactoe['blank4'] == blank_tictactoe['blank5'] == X_O + ' ' or \
            blank_tictactoe['blank6'] == blank_tictactoe['blank7'] == blank_tictactoe['blank8'] == X_O + ' ' or \
            blank_tictactoe['blank0'] == blank_tictactoe['blank3'] == blank_tictactoe['blank6'] == X_O + ' ' or \
            blank_tictactoe['blank1'] == blank_tictactoe['blank4'] == blank_tictactoe['blank7'] == X_O + ' ' or \
            blank_tictactoe['blank2'] == blank_tictactoe['blank5'] == blank_tictactoe['blank8'] == X_O + ' ' or \
            blank_tictactoe['blank0'] == blank_tictactoe['blank4'] == blank_tictactoe['blank8'] == X_O + ' ' or \
            blank_tictactoe['blank2'] == blank_tictactoe['blank4'] == blank_tictactoe['blank6'] == X_O + ' ':
        os.system('cls')
        print('\033[5;36;47m玩家{}赢了，游戏结束\033[0m'.format(X_O))
        time.sleep(5)

        return True


while True:
    print('游戏开始啦')

    blank_tictactoe = {'blank0': '0 ', 'blank1': '1 ', 'blank2': '2 ', 'blank3': '3 ', 'blank4': '4 ', 'blank5': '5 ',
                       'blank6': '6 ', 'blank7': '7 ', 'blank8': '8 '}  # 一个列表，用来存放空的游戏图

    count_playerXO = []  # 一个列表记录所有的棋子的位置
    os.system('cls')
    print_tictactoe()
    chose_mode = input('请选择模式(1)普通玩法 (2)进阶玩法')
    if chose_mode not in ['1', '2']:  # 判断玩家的输入有没有错误
        print('输错了90')
        time.sleep(5)
        continue
    win = bool()
    while True:  # 控制回合

        while True:  # 玩家X回合
            player1 = input('playerX:请输入想下棋的位置0-8')

            if player1 in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
                os.system('cls')
                if player1 not in count_playerXO:  # 判断玩家输入的棋的位置是否已经有了棋子

                    if chose_mode == '2':  # 进阶玩法

                        if len(count_playerXO) > 5:  # 进阶玩法检测是否为六颗棋子在棋盘中，如果超过六颗删除第一颗
                            delete_XO = str(count_playerXO.pop(0))

                            print('消除了', delete_XO, '个格子的', 'X')
                            time.sleep(5)
                            blank_tictactoe['blank' + delete_XO] = str(delete_XO) + ' '
                        if len(count_playerXO) > 4:
                            print('即将删除{}格子的 O'.format(count_playerXO[0]))

                    elif chose_mode == '1':  # 普通玩法
                        pass
                    else:
                        print('输入模式错误')
                        continue

                    if decide(player1, 'X '):
                        count_playerXO.append(player1)

                    win = judge('X')
                    if chose_mode == '1':  # 普通玩法
                        if len(count_playerXO) == 9:  # 标准玩法检测是否平局
                            if not win:
                                print('平局')
                                time.sleep(5)
                                win = True

                    print_tictactoe()

                    break

                else:
                    os.system('cls')
                    print('\033[1;31;47m已经有了3\033[0m')

                    print_tictactoe()

                if win:  # 判断是否有玩家赢了，如果赢了就跳出循环
                    os.system('cls')
                    print_tictactoe()

                    time.sleep(5)
                    break

            else:
                os.system('cls')
                print('\033[1;31;47m输错了2\033[0m')
                print_tictactoe()

        if win:
            time.sleep(5)
            break

        while True:
            player2 = input('playerO:请输入想下棋的位置0-8')
            if player2 in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
                if chose_mode == '1':
                    if len(count_playerXO) == 9:
                        print('平局')
                        break
                if player2 not in count_playerXO:
                    os.system('cls')

                    if chose_mode == '2':

                        if len(count_playerXO) > 5:
                            delete_XO = str(count_playerXO.pop(0))

                            print('消除了', delete_XO, '格子的', 'O')
                            time.sleep(5)
                            blank_tictactoe['blank' + delete_XO] = str(delete_XO) + ' '
                        if len(count_playerXO) > 4:
                            print('即将删除:第{} 个格子的X'.format(count_playerXO[0]))
                    elif chose_mode == '1':  # 普通玩法
                        pass
                    else:
                        print('输入模式错误')
                        continue

                    if decide(player2, 'O '):
                        count_playerXO.append(player2)

                    win = judge('O')
                    if chose_mode == '1':  # 普通玩法
                        if len(count_playerXO) == 9:  # 标准玩法检测是否平局
                            if not win:
                                print('平局')
                                time.sleep(5)
                                win = True

                    print_tictactoe()

                    break

                else:
                    os.system('cls')
                    print('已经有了9')

                    print_tictactoe()

                if win:
                    os.system('cls')
                    print_tictactoe()

                    time.sleep(5)
                    break

            else:
                os.system('cls')
                print('\033[1;31;47m输错了1\033[0m')

                print_tictactoe()
                time.sleep(5)

        if win:
            time.sleep(5)
            break
