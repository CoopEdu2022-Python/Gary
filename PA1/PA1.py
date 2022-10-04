print('游戏开始啦')


def blank_tictactoe(blank11=' ', blank12=' ', blank13=' ', blank21=' ', blank22=' ', blank23=' ', blank31=' ',
                    blank32=' ', blank33=' '):  # 变量作用打印整个表，并填上相应的值
    print('%3s|%3s|%3s' % (blank11, blank12, blank13))
    print('-----------')
    print('%3s|%3s|%3s' % (blank21, blank22, blank23))
    print('-----------')
    print('%3s|%3s|%3s' % (blank31, blank32, blank33))
def panduan(a,b):
    if a == '11':
        blank_tictactoe(blank11=b)
    elif a == '12':
        blank_tictactoe(blank12=b)
    elif a == '13':
        blank_tictactoe(blank13=b)
    elif a == '21':
        blank_tictactoe(blank21=b)
    elif a == '22':
        blank_tictactoe(blank22=b)
    elif a == '23':
        blank_tictactoe(blank23=b)
    elif a == '31':
        blank_tictactoe(blank31=b)
    elif a == '32':
        blank_tictactoe(blank32=b)
    elif a == '33':
        blank_tictactoe(blank33=b)
    else:
        print('输错了')

count_player1 = []
count_player2 = []



player1 = input('请输入行数和列数的组合，如第一行第一列请输入11')
if not player1 in count_player1 and not player1 in count_player2:
    count_player1.append(player1)

else:
    print('已经有了')
for i in count_player1:
    panduan(player1,'* ')

player2 = input('请输入行数和列数的组合，如第一行第一列请输入11')
if not player2 in count_player1 and not player1 in count_player2:
    count_player2.append(player2)

else:
    print('已经有了')
for l in count_player1:
    panduan(l,'@ ')
