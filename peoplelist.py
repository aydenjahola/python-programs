peopleList = [ "Joe Biden", "Donald Trump", "Barack Obama", "Vladimir Putin", "Naftali Bennett", "Mustafa Al-Kadhimi", "Ingrida Šimonytė" ]
print("People List = ", peopleList)
print()
print()
peopleList.append("Micheál Martin")
print("after 'Micheál Martin' was appended to the People List")
print()
print(peopleList)
print()
print()
print("People List = ", peopleList)
print()
print()
peopleList.sort()
print("After sorting into alphabetical order, peopleList is now: ")
print()
print(peopleList)
print()
print()
print("peopleList[0] = ", peopleList[0])
print("peopleList[1] = ", peopleList[1])
print()
print()
print("peopleList.index(Barack Obama) = ", peopleList.index("Joe Biden"))
print()
print()

if "Joe Biden" in peopleList:
    print("'Joe Biden' was found in People List.")
else:
    print("'Joe Biden' was not found in People List.")

print()
print()


if "Brian" in peopleList:
    print("'Brian' was found in People List.")
if "Brian" not in peopleList:
    print("'Brian' was not found in People List.")

print()
print()
print()





another = "yes"

while another != "no":
    nameToLookFor = input("Please enter a name you wish to search for in the list: ")
    if nameToLookFor in peopleList:
        print(nameToLookFor, "was found in People List.", peopleList.index(nameToLookFor))
    else:
        print(nameToLookFor, "was not found in People List.")
    another = input("Do you wish to search the list again? Type yes or no: ")

print("End of Program.")