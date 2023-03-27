mark = int(input("Enter mark: "))

if mark >=80:
    grade = "Distinction."
elif mark >=65:
    grade = "Merit."
elif mark >=50:
    grade = "Pass."
else:
    grade = "Unsuccesful."

print("Your grade is",grade,".")
