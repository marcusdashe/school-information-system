import uuid


class Student:

    @staticmethod
    def generate_student_enrollment_no():
        sid = uuid.uuid4()
        sid_str = str(sid)
        return sid_str[:7]

    def __init__(self, name, age):
        self.name = name
        self.enroll_number = Student.generate_student_enrollment_no()
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)


class StudentInformationSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.enroll_number] = student

    def update_student_details(self, enroll_number, new_name, new_age):
        if enroll_number in self.students:
            student = self.students[enroll_number]
            student.name = new_name
            student.age = new_age
            print("Student details updated")
        else:
            print("Student not found")

    def display_student_information(self, enroll_number):
        if enroll_number in self.students:
            student = self.students[enroll_number]
            print("Name: ", student.name)
            print("Enrollment Number: ", student.enroll_number)
            print("Age: ", student.age)
            print("Grades: ", student.grades)
            print("Average Grade: ", student.calculate_average_grade())
        else:
            print("Student not found")


def main():
    student_list = []
    print("Enter student info... Press Q to Exit")
    while True:
        confirm = input("Press Enter to proceed or Q to exit \n")
        if confirm.lower() in ["q", "quit"]:
            break
        else:
            student_name = input("Student Fullname: ")
            age = input("Student age: ")
            student = Student(student_name, age)
            student_list.append(student)

    if len(student_list) > 0:
        student_info_sys = StudentInformationSystem()
        for student in student_list:
            student_info_sys.add_student(student)
            student_info_sys.display_student_information(student.enroll_number)
            print("\n------------------------------------------------------------\n")

        confirm = input("Press Enter to add Grades to a Student or Q exit: ")
        if confirm.lower() in ["q", "quit"]:
            exit()
        enroll_id = input("Enter Student Enrollment Number: ")
        for student in student_list:
            if student.enroll_number == enroll_id:
                while True:
                    grade = int(input("Enter Student Grade: "))
                    student.add_grade(grade)

                    grade_confirm = input(
                        "Press Enter to proceed or Q to exit \n")
                    if grade_confirm.lower() in ["q", "quit"]:
                        break
                student_info_sys.display_student_information(
                    student.enroll_number)
            else:
                pass


main()
