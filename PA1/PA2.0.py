import os
import time


class PlayerXO:
    def __init__(self, name):
        self.name = name

        self.blank_tictactoe = {'blank0': ' ', 'blank1': ' ', 'blank2': ' ', 'blank3': ' ', 'blank4': ' ',
                                'blank5': ' ',
                                'blank6': ' ', 'blank7': ' ', 'blank8': ' '}
        self.count_playerXO = []

    def decide_location(self, where, what):
        """
         where: 在哪个格子
         b: X or O
        True or False
        """
        if where is None or what is None:
            return False
        for i in range(9):
            if where == self.blank_tictactoe['blank' + str(i)]:
                self.blank_tictactoe['blank' + str(i)] = what
                return True
        else:
            print('输错了')
            return False

    def judge(self):

        if self.blank_tictactoe['blank0'] == self.blank_tictactoe['blank1'] == self.blank_tictactoe['blank2'] == 'X ' or \
                self.blank_tictactoe['blank3'] == self.blank_tictactoe['blank4'] == self.blank_tictactoe[
            'blank5'] == 'X ' or \
                self.blank_tictactoe['blank6'] == self.blank_tictactoe['blank7'] == self.blank_tictactoe[
            'blank8'] == 'X ' or \
                self.blank_tictactoe['blank0'] == self.blank_tictactoe['blank3'] == self.blank_tictactoe[
            'blank6'] == 'X ' or \
                self.blank_tictactoe['blank1'] == self.blank_tictactoe['blank4'] == self.blank_tictactoe[
            'blank7'] == 'X ' or \
                self.blank_tictactoe['blank2'] == self.blank_tictactoe['blank5'] == self.blank_tictactoe[
            'blank8'] == 'X ' or \
                self.blank_tictactoe['blank0'] == self.blank_tictactoe['blank4'] == self.blank_tictactoe[
            'blank8'] == 'X ' or \
                self.blank_tictactoe['blank2'] == self.blank_tictactoe['blank4'] == self.blank_tictactoe[
            'blank6'] == 'X ':
            print('\033[5;36;47m玩家X赢了\033[0m')
            return True
        elif self.blank_tictactoe['blank0'] == self.blank_tictactoe['blank1'] == self.blank_tictactoe[
            'blank2'] == 'O ' or \
                self.blank_tictactoe['blank3'] == self.blank_tictactoe['blank4'] == self.blank_tictactoe[
            'blank5'] == 'O ' or \
                self.blank_tictactoe['blank6'] == self.blank_tictactoe['blank7'] == self.blank_tictactoe[
            'blank8'] == 'O ' or \
                self.blank_tictactoe['blank0'] == self.blank_tictactoe['blank3'] == self.blank_tictactoe[
            'blank6'] == 'O ' or \
                self.blank_tictactoe['blank1'] == self.blank_tictactoe['blank4'] == self.blank_tictactoe[
            'blank7'] == 'O ' or \
                self.blank_tictactoe['blank2'] == self.blank_tictactoe['blank5'] == self.blank_tictactoe[
            'blank8'] == 'O ' or \
                self.blank_tictactoe['blank0'] == self.blank_tictactoe['blank4'] == self.blank_tictactoe[
            'blank8'] == 'O ' or \
                self.blank_tictactoe['blank2'] == self.blank_tictactoe['blank4'] == self.blank_tictactoe[
            'blank6'] == 'O ':
            print('\033[5;36;47m玩家O赢了\033[0m')
            return True

    def print_tictactoe(self):
        print('%3s|%3s|%3s' % (
            self.blank_tictactoe['blank0'], self.blank_tictactoe['blank1'], self.blank_tictactoe['blank2']))
        print('-----------')
        print('%3s|%3s|%3s' % (
            self.blank_tictactoe['blank3'], self.blank_tictactoe['blank4'], self.blank_tictactoe['blank5']))
        print('-----------')
        print('%3s|%3s|%3s' % (
            self.blank_tictactoe['blank6'], self.blank_tictactoe['blank7'], self.blank_tictactoe['blank8']))

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
                if player1 in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
                    if player1 not in count_playerXO:
                        if len(count_playerXO) > 7:
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
                print('\033[5;36;47m玩家X赢了\033[0m')
                break
