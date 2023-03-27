count = 0
sum = 0.0
number = 1
print("Calculates the average mass of the students")
print()
print("Enter 0 to exit the program")
print()

while number != 0:
    number = float(input("Please enter the mass in Kg: "))
    print()
    if number != 0:
        count = count + 1
        sum = sum + number
    if number == 0:
        print("The average mass of the students is {:.2f}".format(sum/count))
        print()

print("Average mass program ended")
