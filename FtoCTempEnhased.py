print("Welcome to Temperature conversion program")
print()
print("This program receives temperature in Fahrenheit and shows Celsius equivalent")
print()
fahrenheitTemp = float(input("Please input Fahrenheit temperature: "))
print()

celsiusTemp = (fahrenheitTemp - 32.0) * 5.0 / 9.0

print(fahrenheitTemp,"degrees Fahrenheit equals",(round(celsiusTemp,2)),"degrees Celsius")
