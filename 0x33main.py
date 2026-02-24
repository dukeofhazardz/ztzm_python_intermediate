import json
import os
from datetime import datetime

FILE_NAME = "students.json"


# ---------------- CUSTOM EXCEPTION ---------------- #
class GradeOutOfRangeError(Exception):
    pass


# ---------------- DECORATOR ---------------- #
def log_operation(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[LOG] Operation recorded at {timestamp}\n")
        return result
    return wrapper


# ---------------- MAIN CLASS ---------------- #
class StudentGradingSystem:
    def __init__(self):
        self.students = []
        self.load_data()

    def load_data(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                self.students = json.load(file)

    def save_data(self):
        with open(FILE_NAME, "w") as file:
            json.dump(self.students, file, indent=4)

    @log_operation
    def add_student(self):
        print("> Enter Student")
        name = input("Name: ")

        while True:
            try:
                grade_input = input("> Enter Grade: ")
                grade = float(grade_input)

                if grade < 0 or grade > 100:
                    raise GradeOutOfRangeError("Grade must be between 0 and 100.")

                break

            except ValueError:
                print("Error: Invalid grade format. Please enter a number.")
            except GradeOutOfRangeError as e:
                print(f"Error: {e}")

        student = {
            "name": name,
            "grade": grade
        }

        self.students.append(student)
        self.save_data()

        print(f"Student {name} recorded.")

    def calculate_average(self):
        if not self.students:
            return 0
        total = sum(student["grade"] for student in self.students)
        return total / len(self.students)

    def student_generator(self):
        for student in self.students:
            yield student

    def generate_report(self):
        print("\n> Student Report")
        for student in self.student_generator():
            print(f"{student['name']} - {student['grade']}")
        print(f"\nAverage Grade: {self.calculate_average():.2f}\n")


# ---------------- MAIN PROGRAM ---------------- #
def main():
    system = StudentGradingSystem()

    while True:
        print("1. Enter Student")
        print("2. View Report")
        print("3. Exit\n")

        choice = input("Choose an option: ")

        if choice == "1":
            system.add_student()
        elif choice == "2":
            system.generate_report()
        elif choice == "3":
            print("Exiting Student Grading System.")
            break
        else:
            print("Invalid option.\n")


if __name__ == "__main__":
    main()