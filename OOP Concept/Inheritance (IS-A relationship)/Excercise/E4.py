class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

class employee(person):
    
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def work(self,task):
        print(f"{self.name} is working on {task}.")

class developer(employee):
    
    def __init__(self, name, age, employee_id, programming_language):
        super().__init__(name, age, employee_id)
        self.programming_language = programming_language

    def code(self,project):
        print(f"{self.name} is coding a project in {self.programming_language}: {project}.")

dev = developer("Bob", 30, "E12345", "Python")
dev.introduce()  # Output: My name is Bob and I am 30 years old.
dev.work("Developing a web application")  # Output: Bob is working on Developing a web application.
dev.code("Building a REST API")  # Output: Bob is coding a project in Python
