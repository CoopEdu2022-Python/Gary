def ShufflingMachine(a, b):
    dict_ = {0: 'S', 1: 'H', 2: 'C', 3: 'D', 4: 'J'}
    dict_ = {i: f'{dict_[i // 13]}{i % 13 + 1}' for i in range(54)}
    res = {}
    n = int(a)
    list_ = [int(_) for _ in b.split(' ')]
    for i in range(a):
        for k, _ in enumerate(list_):
            res[_ - 1] = dict_[k]
        dict_ = res.copy()
    print(*[res[i] for i in sorted(dict_.keys())])


ShufflingMachine(2,
                 '36 52 37 38 3 39 40 53 54 41 11 12 13 42 43 44 2 4 23 24 25 26 27 6 7 8 48 49 50 51 9 10 14 15 16 5 17 18 19 1 20 21 22 28 29 30 31 32 33 34 35 45 46 47')
