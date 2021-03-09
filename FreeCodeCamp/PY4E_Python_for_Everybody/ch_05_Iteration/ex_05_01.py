# Exercise 1: Write a program which repeatedly reads numbers until the
# user enters “done”. Once “done” is entered, print out the total, count,
# and average of the numbers. If the user enters anything other than a
# number, detect their mistake using try and except and print an error
# message and skip to the next number.

# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333

num = 0
total = 0.0

while True:
    usr_input = input("Please enter a number: ")

    if usr_input == 'done':
        break

    try:
        usr_input_data = float(usr_input)
    except:
        print("Please enter a numeric value. Thank you.")
        continue

    num = num + 1
    total = total + usr_input_data

print("\n" + "Total sum of numbers:", str(int(total)) + ", Total numbers entered:", str(num) + ", Average of numbers", str(round((total/num), 2)))
