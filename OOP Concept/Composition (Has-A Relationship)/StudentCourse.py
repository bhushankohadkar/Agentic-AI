class Course:
    def __init__(self,course_name,duration):
        self.course_name = course_name
        self.duration = duration
    def display_course(self):
        print(f"Course Name: {self.course_name}\n Duration: {self.duration} months")

class Student:
    def __init__(self,name,student_id,course):
        self.name = name
        self.student_id = student_id
        self.course = course  # Composition: Student has a Course
    def display_student(self):
        print(f"Student Name: {self.name} \n Student ID: {self.student_id}")
        self.course.display_course()  # Delegating the course display to the Course object

course1 = Course("Python Programming", 3)
student1 = Student("Alice", "S001", course1)  # Creating a Student object
student1.display_student()  # Displaying student and course information