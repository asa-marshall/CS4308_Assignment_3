class Student(object):

    def __init__(self, n, snum, cnum):
        self.name = n
        self.student_num = snum
        self.courses_num = cnum

    def get_name(self):
        return self.name

    def get_student_num(self):
        return self.student_num

    def get_courses_num(self):
        return self.courses_num

    def set_name(self, name):
        self.name = name

    def set_student_num(self, student_num):
        self.student_num = student_num

    def set_courses_num(self, courses_num):
        self.courses_num = courses_num

    def print_values(self):
        print(self.name + ", " + str(self.student_num) + ", " + str(self.courses_num))
