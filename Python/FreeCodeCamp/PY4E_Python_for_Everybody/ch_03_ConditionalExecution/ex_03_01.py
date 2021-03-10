# Exercise 1: Rewrite your pay computation to give the employee 1.5
# times the hourly rate for hours worked above 40 hours.

user_input_hours = input('Enter your hours: ')
user_input_rate = input('Enter your rate: ')
hours = float(user_input_hours)
rate = float(user_input_rate)

if hours > 40 :
    regular_time = hours * rate
    overtime_pay = (hours - 40) * (rate * 0.5)
    pay = regular_time + overtime_pay
else:
    pay = hours * rate

print('\n' + 'Pay:', round(pay, 2))
