from student import Student, student_list


def menu():
    print("\n==============================")
    print(" Student Management System")
    print("==============================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Show Topper")
    print("7. Exit")


def main():

    while True:

        menu()

        try:
            choice = int(input("Enter your choice : "))
        except ValueError:
            print("Invalid Input")
            continue

        if choice == 1:

            roll = int(input("Enter Roll Number : "))

            exists = False
            for s in student_list:
                if s.roll == roll:
                    exists = True
                    break

            if exists:
                print("Roll Number Already Exists")
                continue

            name = input("Enter Name : ")
            marks = int(input("Enter Marks : "))

            if not Student.valid_marks(marks):
                print("Marks should be between 0 and 100")
                continue

            student_list.append(Student(roll, name, marks))
            print("Student Added Successfully")

        elif choice == 2:

            if len(student_list) == 0:
                print("No Students Found")
            else:
                for s in student_list:
                    s.display()

        elif choice == 3:

            roll = int(input("Enter Roll Number : "))

            for s in student_list:
                if s.search_student(roll):
                    s.display()
                    break
            else:
                print("Student Not Found")

        elif choice == 4:

            roll = int(input("Enter Roll Number : "))

            for s in student_list:
                if s.search_student(roll):
                    marks = int(input("Enter New Marks : "))
                    s.update_marks(marks)
                    break
            else:
                print("Student Not Found")

        elif choice == 5:

            roll = int(input("Enter Roll Number : "))

            for s in student_list:
                if s.search_student(roll):
                    s.delete_student()
                    break
            else:
                print("Student Not Found")

        elif choice == 6:

            if len(student_list) == 0:
                print("No Students Found")
            else:
                topper = student_list[0]

                for s in student_list:
                    if s.marks > topper.marks:
                        topper = s

                print("\nTopper Details")
                topper.display()

        elif choice == 7:
            print("Thank You")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()