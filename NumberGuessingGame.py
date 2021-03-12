import random

print("----------------------")
print("Number Guessing Game")
print("----------------------")
guess = int(input("Enter a number between 1-100: "))

rnd_number = random.randint(1, 100)

while guess != rnd_number: 
    if guess < 0 or guess > 100:
        guess = int(input("Enter a number between 1 and 100 !: "))
    
    elif guess < rnd_number:
        guess = int(input("Enter a larger number: "))
    
    else: 
        guess = int(input("Enter a smaller number: "))

print(" _________________________")
print("| Congrulations, you won. |")
print(" ^^^^^^^^^^^^^^^^^^^^^^^^^_")
