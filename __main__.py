from Student import Student


def continue_adding():
    """Prompts user on whether to continue adding students

    :return: bool
    """
    while True:
        print("Input another student? (y/n): ")
        cont = input()
        if not cont == 'n' and not cont == 'y':
            print("Invalid input. Use 'y' or 'n'.")
        elif cont == 'y':
            return True
        else:
            return False


if __name__ == '__main__':
    students = []
    while True:
        student = Student()
        while True:
            try:
                print("Enter name of student: ")
                name = input()
                student.set_name(name)
                break
            except ValueError:
                print("Invalid name argument")
        while True:
            try:
                print("Enter student id number: ")
                student_num = int(input())
                student.set_student_num(student_num)
                break
            except ValueError:
                print("Invalid student_num argument")
        while True:
            try:
                print("Enter number of enrolled courses: ")
                courses = int(input())
                student.set_courses(courses)
                break
            except ValueError:
                print("Invalid courses argument")
        students.append(student)
        if not continue_adding():
            break
    for s in students:
        print(s)
