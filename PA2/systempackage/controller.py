import os


class Controller:
    def __init__(self):
        student_list = []
        officer_list = []
        for i in os.listdir():
            if i.startswith('student_'):
                student_list.append(i[8:-4])
            elif i.startswith('officer_'):
                officer_list.append(i[8:-4])
