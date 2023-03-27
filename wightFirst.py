name = []
student = 1
totalWeight = 0
count = 0
maxWeight = 0
minWeight = 1000

print()
numberOfStudents = int(input("Please enter the number of students in the group: "))
print()

while count < numberOfStudents:
    print()
    print("Student",student)
    nameList = input("Please enter name: ")
    weight = float(input("Please enter weight in kg: "))
    totalWeight = totalWeight + weight


    if weight > maxWeight:
        maxWeight = weight
        heaviestStudent = name
    if weight < minWeight:
        minWeight = weight
        lightestStudent = name


    student = student + 1
    count = count + 1
    print()
        
    
        
        

print()

averageWeight = totalWeight/count

print("Average weight of",count,"students is:",averageWeight,"kg")
print()
print("Heaviest student is",heaviestStudent,"at",maxWeight,"kg")
print("Lightest student is",lightestStudent, "at", minWeight,"kg")

