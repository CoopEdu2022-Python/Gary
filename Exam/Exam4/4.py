def big(num1,num2):

    n1=len(num1.partition('.')[2])
    n2=len(num2.partition('.')[2])
    n=max(n1,n2)
    num1=num1.replace('.','')+('0'*(n-n1))
    num2=num2.replace('.','')+('0'*(n-n2))
    return num1,num2
    sum_final=str(int(num1)+int(num2))
    if n>0:
        sum_final=sum_final[:-n]+'.'+sum_final[-n:]
    return sum_final