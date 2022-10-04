print('游戏开始啦')


def blank_tictactoe(blank11=' ', blank12=' ', blank13=' ', blank21=' ', blank22=' ', blank23=' ', blank31=' ',
                    blank32=' ', blank33=' '):  # 变量作用打印整个表，并填上相应的值
    print('%3s|%3s|%3s' % (blank11, blank12, blank13))
    print('-----------')
    print('%3s|%3s|%3s' % (blank21, blank22, blank23))
    print('-----------')
    print('%3s|%3s|%3s' % (blank31, blank32, blank33))


count_player1 = []
count_player2 = []

blank_tictactoe(blank11='# ')

player1 = input('请输入行数和列数的组合，如第一行第一列请输入21')
if player1 == '11':
    blank_tictactoe(blank11='* ')
elif player1 == '12':
    blank_tictactoe(blank12='* ')
elif player1 == '13':
    blank_tictactoe(blank13='* ')
elif player1 == '21':
    blank_tictactoe(blank21='* ')
elif player1 == '22':
    blank_tictactoe(blank22='* ')
elif player1 == '23':
    blank_tictactoe(blank23='* ')
elif player1 == '31':
    blank_tictactoe(blank31='* ')
elif player1 == '32':
    blank_tictactoe(blank32='* ')
elif player1 == '33':
    blank_tictactoe(blank33='* ')
player2 = input('请输入行数和列数的组合，如第一行第一列请输入21')
if player1 == '11':
    blank_tictactoe(blank11='* ')
elif player1 == '12':
    blank_tictactoe(blank12='* ')
elif player1 == '13':
    blank_tictactoe(blank13='* ')
elif player1 == '21':
    blank_tictactoe(blank21='* ')
elif player1 == '22':
    blank_tictactoe(blank22='* ')
elif player1 == '23':
    blank_tictactoe(blank23='* ')
elif player1 == '31':
    blank_tictactoe(blank31='* ')
elif player1 == '32':
    blank_tictactoe(blank32='* ')
elif player1 == '33':
    blank_tictactoe(blank33='* ')
