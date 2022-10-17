def move(x,direction='right',step=1,list_input=[]):
    if direction == 'right':
        return list_input[-x:]+list_input[:-x]
    elif direction == 'left':
        return list_input[x:]+list_input[:x]
print(move(2,'left',1,[1,2,3,4,5,6,7,8,9]))



