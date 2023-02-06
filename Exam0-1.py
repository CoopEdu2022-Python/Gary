def Sushu(N):
    d=[]
    for i in range(2,N+1):
        for k in range(2,i):
            if not i%k:
                break
        else:
            d.append(i)
    list_=[]
    for i in range(2,len(d)):
        list_.append(d[i]-d[i-1])
    print(list_.count(2))



Sushu(61)

