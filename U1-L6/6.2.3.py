def add_binary(a, b):
    return str(bin(int(a, 2) + int(b, 2))).removeprefix('0b')
