nameList = []
weightList = []
heightList = []
student = 1
totalWeight = 0
count = 0
maxWeight = 0
minWeight = 1000
tallHeight = 0
shortHeight = 250
totalHeight = 0

print()
numberOfStudents = int(input("Please enter the number of students in the group: "))
print()

while numberOfStudents == 0:
    numberOfStudents = int(input("0 is not valid, Please enter the number of students in the group: "))

while count < numberOfStudents:
    print()
    print("Student",student)
    name = input("Please enter the name of the student: ")
    nameList.append(name)
    weight = float(input("Please enter the weight of the student in kg: "))
    weightList.append(weight)
    totalWeight = totalWeight + weight
    height = float(input("Please enter the height of the student in cm: "))
    heightList.append(height)

    if weight > 40 and weight < 200:
        print("Your weight is within the expected range.")
    elif weight < 40:
        print("You are lighter than expected. Please make an appointment with the doctor.")
    elif weight > 200:
        print("You are heavier than expected. Please make an appointment with the doctor.")

    if height > 100 and height <200:
        print("Your height is within the expected range.")
    elif height < 100:
        print("You are shorter than expected. Please don't take any height increasing pills.")
    elif height > 200:
        print("You are taller than average. Please make your way to the NBA (i feel bad about that).")


    if weight > maxWeight:
        maxWeight = weight
        heaviestStudent = name
        
    if weight < minWeight:
        minWeight = weight
        lightestStudent = name

    if height > tallHeight:
        tallHeight = height
        tallestStudent = name

    if height < shortHeight:
        shortHeight = height
        shortestStudent = name



    student = student + 1
    count = count + 1
    print()
        
    
        
        

print()

averageWeight = totalWeight/count
print()
averageHeight = totalHeight/count
print()

print("Average weight of",count,"students is:",averageWeight,"kg")
print()
print("Average height of",count,"students is:",averageHeight,"cm")
print()
print("Heaviest student is",heaviestStudent,"at",maxWeight,"kg")
print("Lightest student is",lightestStudent, "at", minWeight,"kg")
print()
print("The tallest student is",tallestStudent,"at",tallHeight,"cm")
print("The shortest student is",shortestStudent,"at",shortHeight,"cm")
print()
print(nameList)
print(weightList)
print(heightList)

