# Exercise 2: Rewrite your pay program using try and except so that your
# program handles non-numeric input gracefully by printing a message and
# exiting the program. The following shows two executions of the program:

# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input

# Enter Hours: forty
# Error, please enter numeric input

user_input_hours = input('Enter your hours: ')
user_input_rate = input('Enter your rate: ')

try:
    hours = float(user_input_hours)
    rate = float(user_input_rate)
except:
    print('Error, please enter numeric input.')
    quit()

if hours > 40 :
    regular_time = hours * rate
    overtime_pay = (hours - 40) * (rate * 0.5)
    pay = regular_time + overtime_pay
else:
    pay = hours * rate

print('\n' + 'Pay:', round(pay, 2))
