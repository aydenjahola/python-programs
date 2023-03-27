studentList = []
student = 0
numberOfStudents = int(input("How many students in class?: "))
another = "yes"
while student<numberOfStudents:
    name = input("Please give your name: ")
    studentList.append(name)
    student = student+1
print(studentList)


while another != "no":
    nameToLookFor = input("Please enter a name you wish to search for in the list: ")
    if nameToLookFor in studentList:
        print(nameToLookFor,"was found in student list, in location",studentList.index(nameToLookFor))
    else:
        print(nameToLookFor,"was not found in student list.")
    another = input("Do you wish to search the list again? Type yes or no: ")
print("End of Program.")
