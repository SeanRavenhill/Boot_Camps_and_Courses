# Exercise 3:
# Sometimes when programmers get bored or want to have a bit of fun, they add a
# harmless <font color ="red">*Easter Egg*</font> to their program. Modify the
# program that prompts the user for the file name so that it prints a funny
# message when the user types in the exact file name “na na boo boo”.
# The program should behave normally for all other files which exist and
# don’t exist. Here is a sample execution of the program:

# python egg.py
# Enter the file name: mbox.txt
# There were 1797 subject lines in mbox.txt

# python egg.py
# Enter the file name: missing.tyxt
# File cannot be opened: missing.tyxt

# python egg.py
# Enter the file name: na na boo boo
# NA NA BOO BOO TO YOU - You have been punk'd!

# We are not encouraging you to put Easter Eggs in your programs; this is just an exercise.

fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    if fname == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        quit()
    else:
        print("File could not be opened:", fname)
        quit()

count = 0

for line in fhand:
    if not line.startswith("Subject:") : continue
    count = count + 1

print("There were", count,"subject lines in mbox.txt")
