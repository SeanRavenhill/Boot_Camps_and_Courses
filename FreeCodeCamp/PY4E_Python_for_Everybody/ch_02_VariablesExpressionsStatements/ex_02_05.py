# Exercise 5: Write a program which prompts the user for a Celsius temperature,
# convert the temperature to Fahrenheit, and print out the converted temperature.

cel = float(input('Please enter a temperature in C° you wish to convert to F°: '))

print('\n' + str(int(cel)) + 'C° converts to ' + (str(int(cel * 1.8) + 32)) + 'F°')
