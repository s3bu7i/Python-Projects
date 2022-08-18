
import random

number = random.randint(1,100)

a=0
while True:
    a+=1
    guess = int(input("Guess a number :"))
    if number == guess:
        print("You found the correct number, welldone.")
        print(f"It took {a} round.")
        break

    elif guess - number > 30 or number - guess > 30:
        print("Very cold")

    elif guess - number > 20 or number - guess > 20:
        print("Cold")
        
    elif guess - number > 5 or number - guess > 5:
        print("Hot")
        
    elif guess - number >=1 or number - guess >=1:
        print("Very Hot")

    else:
        pass