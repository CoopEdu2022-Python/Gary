age = 20
if age < 1:
    print('婴儿')
elif 1 <= age <= 2:
    print('幼儿')
elif 3 <= age <= 12:
    print('儿童')
elif 13 <= age <= 65:
    if age <= 15:
        print('青春期')
    elif age <= 18:
        print('成年人')
    elif 18 <= age < 20:
        print('青春期成年人')
    elif 20 <= age < 24:
        print('青春期成年人成年人')
    elif 24 <= age < 65:
        print('年轻人成年人')
    elif age >= 65:
        print('老年人')
