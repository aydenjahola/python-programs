nameList = []
heightList = []
student = 1
count = 0
tallHeight = 0
shortHeight = 250
totalHeight = 0

print()
numberOfStudents = int(input("Please enter the number of students in the group: "))
print()

while count < numberOfStudents:
    print()
    print("Student",student)
    name = input("Please enter the name of the student: ")
    nameList.append(name)
    
    height = float(input("Please enter the height of the student in cm: "))
    heightList.append(height)
    totalHeight = totalHeight + height

    
    if height > 100 and height <200:
        print("Your height is within the expected range.")
    elif height < 100:
        print("You are shorter than expected. Please don't take any height increasing pills.")
    elif height > 200:
        print("You are taller than average. Please make your way to the NBA (i feel bad about that).")



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

averageHeight = totalHeight/count
print()

print("Average height of",count,"students is:",averageHeight,"cm")
print()
print("The tallest student is",tallestStudent,"at",tallHeight,"cm")
print("The shortest student is",shortestStudent,"at",shortHeight,"cm")
print()
print(nameList)
print(heightList)

