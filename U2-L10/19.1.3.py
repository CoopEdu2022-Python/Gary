def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        return '除以零了'
    else:
        return result
