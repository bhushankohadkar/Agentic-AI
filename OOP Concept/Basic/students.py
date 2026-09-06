class students:
    def __init__(self, RollNo, name, marks):
        self.RollNo = RollNo
        self.name = name
        self.marks = marks

    def calculate_avg(self):
        return sum(self.marks) / len(self.marks) if self.marks else 0

    def calculate_grade(self):
        avg = self.calculate_avg()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'
    def display_result(self):
        avg = self.calculate_avg()
        grade = self.calculate_grade()
        print(f"Roll No: {self.RollNo}, \nName: {self.name}, \nAverage Marks: {avg:.2f}, \nGrade: {grade}")

student1 = students(1, "Alice", [85, 90, 78])
student1.display_result()
