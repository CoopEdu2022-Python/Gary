def count_operations(self, num1: int, num2: int) -> int:
    while num1 ==0 or num2==0:
        if num1>num2:
            num1-=num2
        else:
            num2-=num1
    return num1+num2