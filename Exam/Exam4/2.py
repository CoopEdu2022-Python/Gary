def reset(login_info):
    while user_name:=input('?'):
        if user_name == 'q':
            return False
        if user_name not in login_info.keys():
            print('?')
        else:
            break
    while password:=input('?'):
        if user_name == 'q':
            return False
        if len(password)<8:
            print('')

