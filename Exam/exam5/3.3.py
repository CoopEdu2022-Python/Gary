def fabonacci(n):
    if n<=2:
        v=1
        return v
    v=fabonacci(n-1)+fabonacci(n-2)
    return v
print(fabonacci(5))