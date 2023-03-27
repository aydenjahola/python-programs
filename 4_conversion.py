def print_topmenu():
    print("Top Level Menu Options:")
    print()
    print("'1' Temperature Conversion")
    print("'2' Distance Conversion")
    print("'3' Mass Conversions")
    print("'4' Volume Conversion")
    print("'5' Area Conversion")
    print("'q' Quit the Program")


def celsius_to_fahrenheit(c_temp):
    return 9.0 / 5.0 * c_temp + 32

def fahrenheit_to_celsius(f_temp):
    return (f_temp - 32.0) * 5.0 / 9.0

def miles_to_kilometres(mi_dist):
    return (mi_dist*1.60934)

def kilometres_to_miles(km_dist):
    return (km_dist*0.621371)

def stones_to_kilograms(st_mass):
    return (st_mass*6.35029)

def kilograms_to_stones(kg_mass):
    return (kg_mass*0.157473)

def litres_to_pints(l_vol):
    return (l_vol*1.75975)

def pints_to_litres(pi_vol):
    return (pi_vol*4.546)

def acres_to_hectares(ac_area):
    return (ac_area*0.404686)

def hectares_to_acres(hec_area):
    return (hec_area*2.47105)


choice = "0"

print_topmenu()

while choice != "q":

    if choice == "1":
        print("temperature Options")
        print()
        print("'c' Convert from Celsius")
        print("'f' Convert from Fahrenheit")
        print("'r' Return to Top Menu")

    if choice == "c":
        c_temp = float(input("Please enter Clesius temperature: "))
        print("Fahrenheit {:.2f}".format(celsius_to_fahrenheit(c_temp)))
        print()
        choice = input("Choose an Options: ")

    elif choice == "f":
        f_temp = float(input("Please enter Fahrenheit temperature: "))
        print("Celsius {:.2f}".format(fahrenheit_to_celsius(f_temp)))
        print()
        choice = input("Choose an Options: ")



    if choice == "2":
        print("Distance Options:")
        print()
        print("'m' Convert from Miles")
        print("'km' Convert from Kilometres")
        print("'r' Return to Top Menu")

    if choice == "m":
        mi_dist = float(input("Please input the distance in Mile: "))
        print((mi_dist),"Miles is equal to {:.2f}".format(miles_to_kilometres(mi_dist)),"Kilometres")
        print()
        choice = input("Choose an Options: ")

    elif choice == "km":
        km_dist = float(input("Please input the distance in Kilometres: "))
        print((km_dist),"Kilometres is equal to {:.2f}".format(kilometres_to_miles(km_dist)),"Miles")
        print()
        choice = input("Choose an Option: ")

    elif choice == "r":
        print_topmenu()

    if choice == "3":
        print("Weight Conversion Options")
        print()
        print("'s' Converts from Stones")
        print("'kg' Converts from Kilograms")
        print("'r' return to Top Menu")

    if choice == "s":
        st_mass = float(input("Please input the mass in Stones: "))
        print((st_mass),"Stones is equal to {:.2f}".format(stones_to_kilograms(st_mass)),"Kilograms")
        print()
        chocie = input("Choose an Option: ")

    elif choice == "kg":
        kg_mass = float(input("Please input the mass in Kilograms: "))
        print((kg_mass),"Kilograms is equal to {:.2f}".format(kilograms_to_stones(kg_mass)),"Stones")
        print()
        chocie = input("Choose an Option: ")

    elif choice == "r":
        print_topmenu()


    if choice == "4":
        print("Volume Conversion Options: ")
        print()
        print("'l' Converts from Litres")
        print("'p' Converts from Pints")
        print("'r' return to Top Menu")

    if choice == "l":
        (l_vol) = float(input("Please input the volume in Litres: "))
        print((l_vol),"Litres is equals to {:.2f}".format(litres_to_pints(l_vol)),"Pints")
        print()
        chocie = input("Choose an Option: ")

    elif choice == "p":
        (pi_vol) = float(input("Please input the volume in Pints: "))
        print((pi_vol),"Pints is equal to {:.2f}".format(pints_to_litres(pi_vol)),"Litres")
        print()
        chocie = input("Choose an Option: ")

    elif choice == "r":
        print_topmenu()


    if choice == "5":
        print("Area Conversion Options: ")
        print()
        print("'ac' Converts from Acres")
        print("'hec' Converts from Hectares")
        print("'r' return to Top Menu")

    if choice == "ac":
        (ac_area) = float(input("Please input the area in Acres: "))
        print((ac_area),"Acres is equals to {:.2f}".format(acres_to_hectares(ac_area)),"Hectares")
        print()
        chocie = input("Choose an Option: ")


    elif choice == "hec":
        (hec_area) = float(input("Please input the area in Hectares: "))
        print((hec_area),"Hectares in equals to {:.2f}".format(hectares_to_acres(hec_area)),"Acres")
        print()
        chocie = input("Choose an Option: ")

    elif choice == "r":
        print_topmenu()



    print()
    choice = input("Please enter your choice from the menu of options: ")
    print()

print("End of Program.")
