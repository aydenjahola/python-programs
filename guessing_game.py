import random
number = random.randint(1, 20)
flag = True
guess = 0

while flag == True:
    guess = int(input("Enter an integer from 1 to 20: "))
    print()
    if guess < number:
        print("Guess is low")
    elif guess > number:
        print("Guess is high")


    else:
        print("You guessed it!")
        flag = False

print("Thank you for using Guessing Game X.")
