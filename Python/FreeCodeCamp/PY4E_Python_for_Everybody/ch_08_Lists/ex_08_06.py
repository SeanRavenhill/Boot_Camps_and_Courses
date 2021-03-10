# Exercise 6: Rewrite the program that prompts the user for a list of numbers
# and prints out the maximum and minimum of the numbers at the end when the
# user enters “done”. Write the program to store the numbers the user enters
# in a list and use the max() and min() functions to compute the maximum and
# minimum numbers after the loop completes.

lst = list()

while True:
    num = input("Enter a number: ")
    if num == "done" or num == "Done" :
        break
    try:
        number = float(num)
    except:
        print("Invalid input")
        continue


    lst.append(number)

print("Maximum is", max(lst))
print("Minimum is", min(lst))
