# Hierarchical Inheritance:

class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f'Initialized School Member: {self.name}')

    def tell(self):
        print(f'Name: {self.name} Age: {self.age}', end=" ")


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        print(f'Initialized Teacher: {self.name}')

    def tell(self):
        super().tell()
        print(f'Salary: {self.salary}')


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks
        print(f'Initialized Student: {self.name}')

    def tell(self):
        super().tell()
        print(f'Marks: {self.marks}')


t = Teacher('Mrs. Smith', 40, 30000)
s = Student('Swaroop', 25, 75)
print()
members = [t, s]
for member in members:
    member.tell()
