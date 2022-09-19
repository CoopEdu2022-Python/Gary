奇数 = 0
偶数 = 0
for i in range(1,101):
    if i%2 == 0:
        偶数 += i
    else:
        奇数 += i
print("奇数和为：",奇数)
print("偶数和为：",偶数)