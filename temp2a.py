def print_options():
    print("Options:")
    print("'p' Print Options")
    print("'c' Convert from Celsius")
    print("'f' Convert from Fahrenheit")
    print("'q' Quit the Program")

def celsius_to_fahrenheit(c_temp):
    return 9.0 / 5.0 * c_temp + 32

def fahrenheit_to_celsius(f_temp):
    return (f_temp - 32.0) * 5.0 / 9.0

choice = "p"

while choice != "q":

    if choice == "c":
        c_temp = float(input("Celsius temperature: "))
        print("Fahrenheit:",round(celsius_to_fahrenheit(c_temp),2))
        print()
        choice = input("Please choose an optionfrom the menu: ")

    elif choice == "f":
        f_temp = float(input("Fahrenheit Temperature: "))
        print("Celsius:",round(fahrenheit_to_celsius(f_temp),2))
        print()
        choice = input("Please choose an optionfrom the menu: ")

    elif choice == "p":
        print_options()
        print()
        choice = input("Please choose an optionfrom the menu: ")
        print()

print("Thank you for using Temperature Conversion Progaram")
