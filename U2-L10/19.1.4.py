class Error(Exception):
    pass


class RadiusError(Error):
    pass


def area(r):
    if r < 0:
        raise RadiusError('半径不能为负数')
    return 3.14 * r ** 2
try:
    area(-10)
except RadiusError:
    print('半径不能为负数')