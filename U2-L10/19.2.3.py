class ScoreError(Exception):
    pass


def input_score():
    score = input('请输入成绩：')
    if not len(score.split(',')[1]) >= 2:
        raise ScoreError
    else:
        return score


try:
    input_score()
except ScoreError:
    print('只能有两位小数')
except ValueError:
    print('请输入数字')
