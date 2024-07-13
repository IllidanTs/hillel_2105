class Student:
    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def change_average_grade(self, new_grade):
        self.average_grade = new_grade

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Average Grade: {self.average_grade}")

student = Student("Mykola", "Parasyk", 20, 85.5)
student.display_info()
student.change_average_grade(90.0)
print("\nAfter changing the average grade:")
student.display_info()
