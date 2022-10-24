def signin(user_info):
    a= input('输入原密码')

    b=input('新密码')
    c=input('重新输入新密码')
    j=[0,1,2,3,4,5,6,7,8,9]
    p=0
    o=0
    t=0



    if not a==user_info['password']:
        print('原密码不对')
        return False
    elif not c==b:
        print('新密码不一致')
        return False






    for i in c:
        if i.isupper():
            p+=1
        if i.islower():
            o+=1
        if i in j:
            t+=1
    if p!=0 and o!=0:
        print('修改成功')
        user_info['password'] = c
        return True

    elif p!=0 and t!=0:
        print('修改成功')
        user_info['password']=c
        return True
    elif o!=0 and t!=0:
        print('修改成功')
        user_info['password'] = c
        return True
    else:
        if p==0:
            print('没有大写')
            return False
        if o==0:
            print('没有小写')
            return False
        if t==0:
            print('没有数字')
            return False
print(signin({'password':'a1234567A'}))