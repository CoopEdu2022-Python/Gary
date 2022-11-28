def calculate_tax(brackets: list[list[int]], income: int) -> float:
    a = []
    for i in range(len(brackets)):

        brackets[i][1] = brackets[i][1]/100

    for i in range(len(brackets)):
        if income - brackets[i][0] >=0 :
            if i ==0:
                a.append(brackets[i][0]*brackets[i][1])
            else:
                a.append((brackets[i][0]-brackets[i-1][0])*brackets[i][1])
        elif brackets[i-1][0]<income and brackets[i][0]>income:
            a.append((brackets[i][0]-income)*brackets[i][1])

    t = 0
    for i in a:
        t+=i
    return t
print(calculate_tax([[3,50],[7,10],[12,25]],10))