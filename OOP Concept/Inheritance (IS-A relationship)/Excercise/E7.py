class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display(self):
        super().display()
        print(f"Student ID: {self.student_id}")

class Researcher(student):
    def __init__(self, name, age, student_id, research_topic):
        super().__init__(name, age, student_id)
        self.research_topic = research_topic

    def display(self):
        super().display()
        print(f"Research Topic: {self.research_topic}")

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display(self):
        super().display()
        print(f"Employee ID: {self.employee_id}")

class Professor(Employee):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age, employee_id)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")

# Example usage
person1 = Person("Alice", 30)
person1.display()

student1 = student("Bob", 20, "S001")
student1.display()

researcher1 = Researcher("Charlie", 25, "S002", "Artificial Intelligence")
researcher1.display()

employee1 = Employee("David", 35, "E001")
employee1.display()

professor1 = Professor("Eve", 40, "E002", "Computer Science")
professor1.display()