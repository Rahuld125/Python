import random

num = random.randint(1, 100)
# print("Random num:", num)

while True:
    num1 = int(input("Guess the secret number :"))
    if num == num1:
        print("Won!")
        break
    elif num1 < num:
        print("Too low, try again!")
    else:
        print("Too high, try again!")
