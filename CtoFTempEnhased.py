print("Welcome to Temperature conversion program")
print()
print("This program receives temperature in Celsius and shows Fahrenheit equivalent")
print()
celsiusTemp = float(input("Please input Celsius temperature: "))
print()

fahrenheitTemp = 5.0 / 9.0 * celsiusTemp + 32

print(celsiusTemp,"degrees celsius equals",(round(fahrenheitTemp,2)),"Fahrenheit")
