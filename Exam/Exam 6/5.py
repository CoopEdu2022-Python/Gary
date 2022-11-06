class Course:
    def __init__(self, cause_name, cause_id, student_list, teacher,grade):
        self.cause_name = cause_name
        self.cause_id = cause_id

        self.student_list = student_list
        self.teacher = teacher
        self.grade = grade
    def get_cause_intro(self):
         print(self.cause_name,self.cause_id,self.student_list,self.teacher,self.grade)
    def stop(self):
        print('You can go out')
    def get_grade(self):
        print(self.grade)
    def assignment(self,assignment_name):
        write = input('Write here: ')
        print(write)

cause1= Course('English', 5001, ['gary','emily','a'], 'A', 100)
cause1.get_cause_intro()
cause1.stop()
cause1.get_grade()
cause1.assignment('write an essay')




