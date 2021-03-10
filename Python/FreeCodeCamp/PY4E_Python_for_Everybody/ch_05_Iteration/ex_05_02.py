# Exercise 2: Write another program that prompts for a list of numbers as
# Exercise 1 did, and at the end prints out both the maximum and minimum of the
# numbers instead of the average.

largest = None
smallest = None

while True:
    num = input("Enter a number: ")

    if num == "done" :
        break

    try:
        number = int(num)
    except:
        print("Please enter a numeric value. Thank you.")
        continue

    if largest is None or largest < number :
        largest = number

    if smallest is None or smallest > number :
        smallest = number

print("\n" + "Maximum is", largest)
print("Minimum is", smallest)
