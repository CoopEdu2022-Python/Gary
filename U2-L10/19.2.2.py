class GetFloatError(Exception):
    pass


def float_input(a):
    if type(a) == float:
        raise GetFloatError()

    return a
try:
    float_input(1)
except GetFloatError:
    print('not float')


