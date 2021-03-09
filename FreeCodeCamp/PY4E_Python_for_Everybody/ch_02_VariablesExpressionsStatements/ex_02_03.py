# Exercise 3: Write a program to prompt the user for hours and rate per hour
# to compute gross pay.

# We won’t worry about making sure our pay has exactly two digits after the
# decimal place for now. If you want, you can play with the built-in Python
# round function to properly round the resulting pay to two decimal places.

hours = input('Enter your hours: ')
rate = input('Enter your rate: ')
pay = float(hours) * float(rate)

print('\n' + "Pay:", round(pay, 2))
