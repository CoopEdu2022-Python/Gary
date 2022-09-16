age = 10
if age < 1:
    print('婴儿')
elif age >=1 and age <=2:
    print('幼儿')
elif age >=3 and age <=12:
    print('儿童')
elif age >=13 and age<=65:
    if age <=15:
        print('青春期')
    elif age <=18:
        print('成年人')
    elif age <= 18 and age>=20:
        print('青春期成年人')
    elif age<=20 and age>=24:
        print('青春期成年人成年人')
    elif age<=24 and age>=64:
        print('年轻人成年人')
    elif age ==65:
        print('老年人')
