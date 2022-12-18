import os


class Course:
    course_list = []
    for i in os.listdir():
        if i[0:7] == 'course_':
            course_list.append(i[7:-4])
    print(course_list)

    @staticmethod
    def create_course(name, student_list, teacher, course_type, credit, student_num):

        if name not in Course.course_list:
            with open('course_' + name + '.txt', 'w') as course_info:

                course_info.write('Course name: ' + name + '\n')
                course_info.write('Teacher: ' + teacher + '\n')
                course_info.write('Course type: ' + course_type + '\n')
                course_info.write('Credit: ' + str(credit) + '\n')
                course_info.write('Student number: ' + str(student_num) + '\n')
                student_list = ''.join(str(i) + ',' for i in student_list)
                course_info.write('Student list: {}\n'.format(student_list))

                print('课程创建成功')
                return True

        else:
            print('名称已经用过')
            return False



