class Course:
    def __init__(self, name, studentlist, teacher, coursetype, credit):
        self.studentlist = studentlist
        self.teacher = teacher
        self.coursetype = coursetype
        self.credit = credit
        self.name = name

    def addstudent(self, student):
        pass

    def deletestudent(self, student):
        pass


class Student:
    def __init__(self, name):
        self.name = name

    def addcourse(self, course):
        pass

    def dropcourse(self, course):
        pass

    def seestucourse(self, course):
        pass

    def seerequire(self):
        pass

    def credir(self):
        pass


class InSystem:
    def __init__(self, type, state):
        self.type = type
        self.state = state

    def isright(self):
        pass

    def reset(self):
        pass


class Officer:
    def __init__(self, name):
        self.name = name

    def createcourse(self):
        pass

    def setcredit(self, credit):
        pass

    def seeprofile(self):
        pass

    def creatstudent(self,name,credit):

        pass
    def changecourse(self):
        pass

    def seecourse(self):
        pass
    def seestucourse(self):
        pass