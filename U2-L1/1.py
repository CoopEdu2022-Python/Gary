class Student:
    def __init__(self,id,name,course):
        self.id = id
        self.name = name
        self.course = course
    def add_course(self,course):
        self.course.append(course)
    def drop_course(self,course):
        if course in self.course:
            self.course.remove(course)
        else:
            print('你没有这门课')
class Course:
    def __init__(self,name,id,student):
        self.name = name
        self.id = id
        self.student = student
    def add_student(self,student):
        self.student.append(student)
    def drop_student(self,student):
        if student in self.student:
            self.student.remove(student)
        else:
            print('这个学生没有这门课')
Student1 = Student(1,'gary',[1001,'Math'])

