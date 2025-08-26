
# Inheritance : It is a powerful feature of Object Oriented Programming.

# 1. Single Inheritance
class Animal:
    def eat(self):
        print("Animal eats")

    def sleep(self):
        print("Animal sleeps")


class Bird(Animal):
    def set_type(self, type):
        self.type = type

    def fly(self):
        print("It flies in the sky")

    def __str__(self):
        return "This is a " + self.type


duck = Bird()
duck.set_type("Duck")
print(duck)
duck.eat()
duck.sleep()
duck.fly()
