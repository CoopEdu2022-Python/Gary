"""
fileObject.seek(offset[, whence])
offset -- 开始的偏移量，也就是代表需要移动偏移的字节数

whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。


"""
a = open("21.1.1", "r+")
a.seek(1, 0)    #从文件开头开始算起，偏移1个字节
print(a.read())
a.close()
