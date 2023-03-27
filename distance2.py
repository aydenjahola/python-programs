def print_options():
    print("Options:")
    print("'p' print options")
    print("'m' convert from miles")
    print("'k' convert from kilometres")
    print("'q' quit the program")

def miles_to_kilometres(miles):
    return miles*1.60934

def kilometres_to_miles(kilometres):
    return kilometres*0.621371

choice = "p"

while choice != "q":

    if choice == "m":
        miles = float(input("Please enter distance in miles: "))
        print("Kilometres:",round(miles_to_kilometres(miles),2))
        print()
        choice = input("pelase choose an option from the menu: ")

    elif choice == "k":
        kilometres = float(input("Please enter distance in kilometres: "))
        print("Miles:",round(kilometres_to_miles(kilometres),2))
        print()
        chocie = input("pelase choose an option from the menu: ")

    elif choice == "p":
        print_options()
        print()
        choice = input("Please choose an option from the menu: ")

print("Program run ended. Thank you for using Distance Calculator.")
