student_list = []


class Student:

    total_students = 0

    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        Student.total_students += 1

    @staticmethod
    def valid_marks(marks):
        return 0 <= marks <= 100

    @classmethod
    def show_total_students(cls):
        print("Total Students :", cls.total_students)

    def grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 40:
            return "D"
        else:
            return "Fail"

    def display(self):
        print("---------------------------")
        print("Roll No :", self.roll)
        print("Name    :", self.name)
        print("Marks   :", self.marks)
        print("Grade   :", self.grade())
        print("---------------------------")

    def search_student(self, roll):
        return self.roll == roll

    def update_marks(self, marks):
        if Student.valid_marks(marks):
            self.marks = marks
            print("Marks Updated Successfully")
        else:
            print("Invalid Marks")

    def delete_student(self):
        student_list.remove(self)
        Student.total_students -= 1
        print("Student Deleted Successfully")