class Class:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

class Student(Class):
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def introduce(self):
         print(
            f"My name is {self.name} and I am {self.age} years old. "
            f"I am a student with ID: {self.student_id}"
        )
    def study(self,course):
        print(f"{self.name} is studying {course}.")


student = Student("Alice", 20, "S12345")
student.introduce()  # Output: My name is Alice and I am 20 years old. I am a student with ID: S12345
student.study('Python')      # Output: Alice is studying Python.