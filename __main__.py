"""__main__

Prompts user to enter information about one or more students and prints back the entered information.
"""
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
    # Define an array of students
    students = []

    while True:
        # create a Student object
        student = Student()

        # request name from input
        while True:
            try:
                print("Enter name of student: ")
                name = input()
                # invoke a method to change the value of its attributes of the object
                student.set_name(name)
                break
            except ValueError:
                print("Invalid name argument")

        # request student number from input
        while True:
            try:
                print("Enter student id number: ")
                student_num = int(input())
                # invoke a method to change the value of its attributes of the object
                student.set_student_num(student_num)
                break
            except ValueError:
                print("Invalid student_num argument")

        # request courses from input
        while True:
            try:
                print("Enter number of enrolled courses: ")
                courses = int(input())
                # invoke a method to change the value of its attributes of the object
                student.set_courses(courses)
                break
            except ValueError:
                print("Invalid courses argument")

        # store the Student in the array
        students.append(student)
        if not continue_adding():
            break

    # invoke a method that displays the value of each attribute of every student in the array
    print("\nPrinting student information...")
    for s in students:
        print(s)
