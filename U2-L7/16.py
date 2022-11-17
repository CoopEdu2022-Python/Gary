class list:
    def __init__(self):
        self.list = []
        self.length = 0
        self.front = 0

    def append(self, value):
        self.list.append(value)
        self.length = self.length + 1

    def delappend(self):
        a = self.list.pop(self.front)
        self.length = self.length - 1
        self.front = self.front + 1
        return a

    def peek(self):
        return self.list[0]

