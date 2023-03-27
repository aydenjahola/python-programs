def print_topmenu():
    print("Top Level Menu Options:")
    print()
    print("'1' Area & Perimeter of Square ")
    print("'2' Area & Perimeter of Rectangle ")
    print("'3' Area & Perimeter of Circle")
    print("'q' Quit the Program")


PI = 3.141592653589793238

choice = "0"

print_topmenu()

while choice != "q":

    if choice == "1":
        print("Area of Square")
        print()
        side = float(input("Please enter the length of the square's side: "))
        print()
        area = side*side
        perimeter = 4*side
        print("The area of the square is: {:.2f}".format(area),"square metres")
        print("The perimeter of the square is: {:.2f}".format(perimeter),"metres")


    if choice == "2":
        print("Area of Rectangle:")
        print()
        length = float(input("Please enter the length of the rectangle: "))
        width = float(input("Please enter the width of the rectangle: "))
        area = length*width
        perimeter = 2*(length+width)
        print()
        print("The area of the rectangle is: {:.2f}".format(area),"square metres")
        print("The perimeter of the rectangle is: {:.2f}".format(perimeter),"metres")

    if choice == "3":
        print("Area of Circle")
        print()
        r = float(input("Please enter the radius of the circle: "))
        area = PI*r*r
        perimeter = 2*PI*r
        print()
        print("The area of the circle is: {:.2f}".format(area),"square metres")
        print("The perimeter of the circle is: {:.2f}".format(perimeter),"metres")
    
    print()
    choice = input("Please enter your choice from the menu of options: ")
    print()

print("End of Program.")
        
        
