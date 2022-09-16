has_ticket = True
knife_length = 2000
if has_ticket:
    print('有车票，可以安检')
    if knife_length >= 20:
        print('不许携带%d米的刀进站' % knife_length)
    else:
            print('安检通过')

else:
    print('可以进站')

has_ticket = True
knife_length = 2000
if has_ticket and knife_length<20:
    print('旅行愉快')
elif not has_ticket:
    print('先买票')
elif knife_length >= 20:
    print('不许携%d厘米的到上车'%knife_length)
