from Student import Student


def continue_adding():
    """Prompts user on whether to continue adding students

    :return: bool
    """
    while True:
        print("Input another student? (y/n): ")
        contin = input()
        if not contin == 'n' and not contin == 'y':
            print("Invalid input. Use 'y' or 'n'.")
        elif contin == "y":
            return True
        else:
            return False


if __name__ == '__main__':
    students = []
    while True:
        print("Enter name of student: ")
        name = input()
        print("Enter student id number: ")
        student_num = input()
        print("Enter number of enrolled courses: ")
        courses_num = input()
        student = Student(name, student_num, courses_num)
        students.append(student)
        cont = continue_adding()
        if not cont:
            break
    for s in students:
        s.print_values()




