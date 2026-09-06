class Manager:
    def calculate_salary(self, base_salary, bonus):
        return base_salary + bonus  # Managers get a bonus of 1000
class Developer:
    def calculate_salary(self, base_salary, overtime):
        return base_salary + (overtime * 15)  # Developers get paid for overtime hours
class Designer:
    def calculate_salary(self, base_salary, commission):
        return base_salary + (commission * 0.1)  # Designers get a commission of 10% of their sales


employees = [
    Manager(),
    Developer(),
    Designer()
]

for employee in employees:
    print(employee.calculate_salary(50000, 1000))