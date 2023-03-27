passes = 0
unsuccessful = 0
count = 1

while count <=5:
     result = int(input("Please enter the result: "))

     if result >= 50:
         passes = passes + 1

     else:
        unsuccessful = unsuccessful + 1

     count = count + 1

print("Nubmer of Passes:",passes)
print("Nubmer of Unsuccessful:",unsuccessful)
