num_list=[1,2,3,4,5,6,7,8,9,10]
b=[]
d=[]
for a in range(0,len(num_list)-2):
    for b in range(a+1,len(num_list)-1):
        for c in range(b+1,len(num_list)):
            k=num_list[a]*num_list[b]*num_list[c]
            d.append(k)
print(max(d))



