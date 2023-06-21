class Student:
    def _init_(self, name, roll_number, age):
        self.name = name
        self.roll_number = roll_number
        self.age = age

class StudentManagementSystem:
    def _init_(self):
        self.students = []

    def add_student(self):
        name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")
        age = input("Enter student age: ")
        student =Student(name, roll_number)
        self.students.append(student)
        print("Student added successfully.")

    def display_students(self):
        if not self.students:
            print("No students found.")
        else:
            for student in self.students:
                print("Name:", student.name)
                print("Roll Number:", student.roll_number)
                print("Age:", student.age)
                print("---------------------")

    def search_student(self):
        roll_number = input("Enter roll number to search: ")
        found = False
        for student in self.students:
            if student.roll_number == roll_number:
                print("Student found!")
                print("Name:", student.name)
                print("Roll Number:", student.roll_number)
                print("Age:", student.age)
                found = True
                break
        if not found:
            print("Student not found.")

    def menu(self):
        while True:
            print("===== Student Management System =====")
            print("1. Add Student")
            print("2. Display Students")
            print("3. Search Student")
            print("4. Quit")
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.display_students()
            elif choice == '3':
                self.search_student()
            elif choice == '4':
                print("Thank you for using the Student Management System.")
                break
            else:
                print("Invalid choice. Please try again.")

# Create an instance of StudentManagementSystem and run the program
sms = StudentManagementSystem()
sms.menu()