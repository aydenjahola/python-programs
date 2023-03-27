import random

another = "y"

while another != "n":
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    print("You threw",num1,"and",num2)
    print()

    score = num1 + num2
    if num1 == num2:
        print("You threw a double")
        print("Your score is:", 2*score)
        print()

    else:
        print("Your score is:",score)
        print()

    another = input("Would you like to throw 2 more dices? Type y (for yes) or n (for no): ")
    print()

print("End of Program.")
