a=[445,3,56,67]
b=[]
for i in a:
    b.append(i)
    if not i==a[-1]:
        b.append(0)
print(b)