class Father:
    def __init__(self, father_name):
        self.father_name = father_name
    def father_skill(self):
        print("Father's skill is painting.")

class mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name
    def mother_skill(self):
        print("Mother's skill is cooking.")

class child(Father, mother):
    def __init__(self, father_name, mother_name, child_name):
        Father.__init__(self, father_name)
        mother.__init__(self, mother_name)
        self.child_name = child_name

    def child_skill(self):
        print("Child's skill is dancing.")

child1 = child("John", "Jane", "Alice")
print("Father's Name:", child1.father_name)  
print("Mother's Name:", child1.mother_name)
child1.father_skill()
child1.mother_skill()
child1.child_skill()

mother1 = mother("Jane")
print("Mother's Name:", mother1.mother_name)
mother1.mother_skill()