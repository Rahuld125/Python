# This script demonstrates how to merge two dictionaries in Python.
students = {101: "Amit", 102: "Deepak", 103: "Ravi"}
students2 = {103: "Kiran", 104: "Atul", 101: "Ajay"}
students.update(students2)
print(students)
