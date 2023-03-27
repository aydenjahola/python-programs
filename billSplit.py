print("Welcome to bill calculation program")

bill = float(input("Please enter bill amount: "))
tipPercentage = float(input("What percentage tip are you going to give? Enter number as e.g., 0.10 for 10%: "))
numberOfPeople = float(input("How many people are going to split the bill? "))

total = bill + (bill * tipPercentage)

eachPay = total / numberOfPeople

print()

print("The total amount of the bill is:",total,"Euro.")

print("The total share for each person comes to:",eachPay)

print("Rounded to show whole Cents:",round(eachPay,2))
