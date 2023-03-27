import random
number = random.randint(1, 9)
flag = True
guess = 0

while flag == True:
    guess = int(input("Enter an integer from 1 to 9: "))
    print()
    if guess < number:
        print("it's Bigger...")
        print()
    elif guess > number:
        print("it's not so big...")
        print()


    else:
        print("Hooray! You guesses it right")
        flag = False

print("Thank you for using Guessing Game.")
