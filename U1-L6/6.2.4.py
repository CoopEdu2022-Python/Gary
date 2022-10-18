a=6
b=[]
if a//1000!=0:
    b.append('M'*(a//1000))
    a=a%1000
if a//500!=0:
    b.append('D'*(a//500))
    a=a%500
if a//100!=0:
    b.append('C'*(a//100))
    a=a%100
if a//50!=0:
    b.append('L'*(a//50))
    a=a%50
if a//10!=0:
    b.append('X'*(a//10))
    a=a%10
if a//5!=0:
    b.append('V'*(a//5))
    a=a%5
if a//1!=0:
    b.append('I'*(a//1))
    a=a%1
if 'IIII' in b:
    b[b.index('IIII')]='IV'
if 'VIV' in b:
    b[b.index('VIV')]='IX'
if 'XXXX' in b:
    b[b.index('XXXX')]='XL'
if 'LXL' in b:
    b[b.index('LXL')]='XC'
if 'CCCC' in b:
    b[b.index('CCCC')]='CD'
if 'DCD' in b:
    b[b.index('DCD')]='CM'
print(''.join(b))
