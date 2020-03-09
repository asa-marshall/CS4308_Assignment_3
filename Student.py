class Student(object):
    """Student class

    Contains data for three values:
    name: name of student
    student_num: student number
    courses: number of enrolled courses
    """

    def __init__(self, name="", student_num=0, courses=0):
        """Constructor

        :param name: not null str
        :param student_num: not null int
        :param courses: not null int
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
        """Returns the name the student

        :return: str
        """
        return self.name

    def get_student_num(self):
        """Returns the student number

        :return: int
        """
        return self.student_num

    def get_courses(self):
        """Returns the student's number of enrolled courses

        :return: int
        """
        return self.courses

    def set_name(self, name):
        """Sets the student name to the str passed as a parameter

        :param name: not null str
        :return: void
        """
        if name is None or not isinstance(name, str):
            raise ValueError("invalid name argument")
        self.name = name

    def set_student_num(self, student_num):
        """Sets the student number to the int passed as a parameter

        :param student_num: not null int
        :return: void
        """
        if student_num is None or not isinstance(student_num, int):
            raise ValueError("invalid student_num argument")
        self.student_num = student_num

    def set_courses(self, courses):
        """Sets the student's number of enrolled courses to the int passed as a paramter

        :param courses: not null int
        :return: void
        """
        if courses is None or not isinstance(courses, int):
            raise ValueError("invalid courses argument")
        self.courses = courses

    def __repr__(self):
        """Returns a str representation of the student

        :return: str
        """
        return self.name + ", " + str(self.student_num) + ", " + str(self.courses)
