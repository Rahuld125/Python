# Multilevel inheritance example

class Persion:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Person constructor called")

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Emp(Persion):
    def __init__(self, name, age, id, sal):
        super().__init__(name, age)
        self.id = id
        self.sal = sal
        print("Employee constructor called")

    def income(self):
        return self.sal

    def __str__(self):
        return f"{super().__str__()}, Emp ID: {self.id}, Salary: {self.sal}"


class Manager(Emp):
    def __init__(self, name, age, id, sal, bonus):
        super().__init__(name, age, id, sal)
        self.bonus = bonus
        print("Manager constructor called")

    def income(self):
        return super().income() + self.bonus

    def __str__(self):
        return f"{super().__str__()}, Bonus: {self.bonus}"


m = Manager("John", 35, 101, 50000, 10000)
print(m)
print("Manager's Salary:", Emp.income(m))
print("Manager's Total Salary :", m.income())
