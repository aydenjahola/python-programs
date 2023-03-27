totalmarks = int(input("Please enter your total marks: "))
     
if totalmarks >= 540:
    print("Congratualations!")
    print("you are eligible for a full scholarship.")
elif totalmarks >= 480:
    print("Congratulations!")
    print("your are eligible for a 50 percent scholarship.")
elif totalmarks >= 400:
    print("Congratulations!")
    print("you are eligible for a 10 percent scholarship.")
else:
    print("We regret that you are not eligible for a scholarship.")
    print("we are sorry.")
