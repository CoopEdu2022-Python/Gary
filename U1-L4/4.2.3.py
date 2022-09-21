def make_shirt(a,b='I love Python'):
    return '尺码%s，文字%s'%(a,b)
print(make_shirt('大'))
print(make_shirt('中'))
print(make_shirt('小','hi'))