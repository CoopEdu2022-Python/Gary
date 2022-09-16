homework=True
homework_score = 70

if homework ==True and homework_score>=1:
    print('可以进校')
elif not homework==True and homework_score>=1:
    print('没交作业')
elif homework==True and homework_score<=1:
    print('没写')
