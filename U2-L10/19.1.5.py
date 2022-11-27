def num5(sentence):
    no5number = Exception('不足或超过5个数字')
    sentence.split(',')
    if len(sentence) != 5:
        raise no5number

    for i in sentence:
        if not type(i) == int:
            raise no5number
        else:
            print(sentence)