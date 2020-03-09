class Student(object):

    def __init__(self, name="", student_num=0, courses=0):
        """Constructor

        :param name: name of student
        :param student_num: student id
        :param courses: number of enrolled courses
        """
        if name is None or not isinstance(name, str):
            raise ValueError("invalid name argument")
        if student_num is None or not isinstance(student_num, int):
            raise ValueError("invalid student_num argument")
        if courses is None or not isinstance(courses, int):
            raise ValueError("invalid courses argument")
        self.name = name
        self.student_num = student_num
        self.courses = courses

    def get_name(self):
        return self.name

    def get_student_num(self):
        return self.student_num

    def get_courses(self):
        return self.courses

    def set_name(self, name):
        if name is None or not isinstance(name, str):
            raise ValueError("invalid name argument")
        self.name = name

    def set_student_num(self, student_num):
        if student_num is None or not isinstance(student_num, int):
            raise ValueError("invalid student_num argument")
        self.student_num = student_num

    def set_courses(self, courses):
        if courses is None or not isinstance(courses, int):
            raise ValueError("invalid courses argument")
        self.courses = courses

    def __repr__(self):
        return self.name + ", " + str(self.student_num) + ", " + str(self.courses)
