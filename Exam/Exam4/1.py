
def chang_list(x, direction='right', list_input=[]):
    new_list = []
    if direction == 'left':
        for d in list_input[0:x]:
            list_input.append(d)
        for i in range(x):
            list_input.pop(0)
        return list_input
    elif direction == 'right':

        for f in list_input[-1:-x]:
            list_input.append(f)
        for i in range(x):
            list_input.pop(0)
        return list_input

print(chang_list(2 ,'left'))
